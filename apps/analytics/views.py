from django.shortcuts import render
from rest_framework import viewsets
from .models import BiDataset, BiMetric
from .serializers import BiDatasetSerializer, BiMetricSerializer
from django.http import JsonResponse
import requests
import yfinance as yf

# Create your views here.

class BiDatasetViewSet(viewsets.ModelViewSet):
    queryset = BiDataset.objects.all()
    serializer_class = BiDatasetSerializer

class BiMetricViewSet(viewsets.ModelViewSet):
    queryset = BiMetric.objects.all()
    serializer_class = BiMetricSerializer
    
def indice_oportunidad_etf(request):
    try:
        # 1. EXTRAER: Valor del dólar en Chile
        respuesta_dolar = requests.get('https://mindicador.cl/api/dolar', timeout=15)
        respuesta_dolar.raise_for_status()
        precio_dolar_clp = respuesta_dolar.json()['serie'][0]['valor']

        # 2. EXTRAER: Precios de los fondos
        tickers = ['VOO', 'QQQM', 'VXUS']
        resultados = []

        for ticker in tickers:
            fondo = yf.Ticker(ticker)
            
            # EL ARREGLO: Pedimos 5 días para asegurar que siempre haya un historial válido
            historial = fondo.history(period="5d")
            
            # Verificamos que al menos existan 2 días para poder comparar
            if len(historial) >= 2:
                # .iloc[-2] trae el penúltimo día, .iloc[-1] trae el último (hoy)
                precio_ayer_usd = historial['Close'].iloc[-2]
                precio_hoy_usd = historial['Close'].iloc[-1]
            else:
                # Respaldo extremo: si por alguna razón falla, igualamos precios
                precio_ayer_usd = historial['Close'].iloc[-1]
                precio_hoy_usd = historial['Close'].iloc[-1]
            
            # 3. TRANSFORMAR
            variacion_usd = precio_hoy_usd - precio_ayer_usd
            costo_real_clp = precio_hoy_usd * precio_dolar_clp
            
            es_buen_momento = bool(variacion_usd < 0) 
            precio_seguro = float(round(precio_hoy_usd, 2))
            costo_seguro = int(round(costo_real_clp, 0))

            resultados.append({
                'fondo': ticker,
                'precio_usd': precio_seguro,
                'costo_clp': costo_seguro,
                'en_oferta': es_buen_momento
            })

        # 4. CARGAR
        return JsonResponse({'dolar_hoy': precio_dolar_clp, 'oportunidades': resultados})

    except Exception as e:
        return JsonResponse({'error': 'Fallo en la matriz de datos', 'detalle': str(e)}, status=503)

def obtener_datos_financieros(request):
    url = 'https://mindicador.cl/api/dolar'
    
    try:
        # Intentamos conectarnos a la API externa
        respuesta = requests.get(url, timeout=15) # El timeout evita que se quede pegado infinito
        respuesta.raise_for_status() # Verifica si mindicador devolvió un error (ej. 404 o 500)
        datos = respuesta.json()
        
        ultimos_dias = datos['serie'][:7]
        ultimos_dias.reverse() 
        
        dias = [dia['fecha'][8:10] + "-" + dia['fecha'][5:7] for dia in ultimos_dias]
        valores = [dia['valor'] for dia in ultimos_dias]
            
        return JsonResponse({'fechas': dias, 'valores': valores})
        
    except requests.exceptions.RequestException as e:
        # Si la API externa falla, devolvemos un JSON de error controlado para que Vue no explote
        return JsonResponse(
            {'error': 'No se pudieron obtener los datos financieros en este momento.', 'detalle': str(e)}, 
            status=503 # 503 = Service Unavailable
        )
        
