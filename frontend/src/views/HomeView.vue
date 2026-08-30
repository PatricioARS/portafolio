<script setup>
import { ref, onMounted, onUnmounted, nextTick, computed, watch } from 'vue';
import 'echarts';

let observadorDeScroll;

// --- DATOS DE PROYECTOS Y CATEGORÍAS ---
const misProyectos = ref([]);
const categorias = ref([{ id: 0, name: 'Todos' }]);
const filtroActual = ref('Todos'); 

const cargarCategorias = async () => {
  try {
    const respuesta = await fetch('/api/v1/portafolio/categorias/');
    const datos = await respuesta.json();
    categorias.value = [{ id: 0, name: 'Todos' }, ...datos];
  } catch (error) {
    console.error("Error al cargar categorías:", error);
  }
};

const cargarProyectos = async () => {
  try {
    const respuesta = await fetch('/api/v1/portafolio/proyectos/');
    const datos = await respuesta.json();
    misProyectos.value = datos;

    await nextTick();
    if (observadorDeScroll) {
      document.querySelectorAll('.reveal').forEach((elemento) => {
        observadorDeScroll.observe(elemento);
      });
    }
  } catch (error) {
    console.error("Error al cargar los proyectos:", error);
  }
};

const proyectosFiltrados = computed(() => {
  if (filtroActual.value === 'Todos') return misProyectos.value; 
  return misProyectos.value.filter(proyecto => proyecto.category && proyecto.category.name === filtroActual.value);
});

watch(proyectosFiltrados, async () => {
  await nextTick();
  if (observadorDeScroll) {
    document.querySelectorAll('.reveal').forEach((elemento) => {
      observadorDeScroll.observe(elemento); 
    });
  }
});

// --- MOTOR DE LA MÁQUINA DE ESCRIBIR ---
const roles = ["Ingeniero en Informática", "Developer", "Arquitecto de Software", "Analisis de Datos", "Soporte en TI", "Arquitectura Cloud", "Python manage.py runserver"];
const textoActual = ref('');
const indiceRol = ref(0);
const borrando = ref(false);
let timerMaquinaEscribir; 

const escribir = () => {
  const fraseActual = roles[indiceRol.value];
  if (borrando.value) {
    textoActual.value = fraseActual.substring(0, textoActual.value.length - 1);
  } else {
    textoActual.value = fraseActual.substring(0, textoActual.value.length + 1);
  }
  let velocidad = borrando.value ? 50 : 100;
  if (!borrando.value && textoActual.value === fraseActual) {
    velocidad = 2000;
    borrando.value = true;
  } else if (borrando.value && textoActual.value === '') {
    borrando.value = false;
    indiceRol.value = (indiceRol.value + 1) % roles.length;
    velocidad = 500;
  }
  timerMaquinaEscribir = setTimeout(escribir, velocidad);
};

// --- EFECTO GLITCH (TÍTULO PRINCIPAL) ---
const palabrasPrincipales = ["Hola, soy", "Patricio Riquelme Saez", "Ingeniero en Informática", "Developer"];
const textoPrincipal = ref(palabrasPrincipales[0]); 
let indicePalabra = 0;
const caracteresHacker = "!<>-_\\/[]{}—=+*^?#_"; 
let timerGlitch;

const iniciarEfectoGlitch = () => {
  indicePalabra = (indicePalabra + 1) % palabrasPrincipales.length;
  const palabraDestino = palabrasPrincipales[indicePalabra];
  let iteracion = 0;
  const intervalo = setInterval(() => {
    textoPrincipal.value = palabraDestino.split("").map((letra, index) => {
      if (index < iteracion || palabraDestino[index] === " ") return palabraDestino[index];
      return caracteresHacker[Math.floor(Math.random() * caracteresHacker.length)];
    }).join("");

    if (iteracion >= palabraDestino.length) {
      clearInterval(intervalo);
      timerGlitch = setTimeout(iniciarEfectoGlitch, 4000); 
    }
    iteracion += 1 / 3; 
  }, 30);
};

// --- PERFIL Y ECHARTS ---
const miPerfil = ref({ fullname: 'Cargando...', headline: '...', bio: 'Conectando con el servidor...', cv_url: '#', social_links: [] });

const chartOption = ref({
  tooltip: { trigger: 'axis' },
  grid: { left: '5%', right: '5%', bottom: '5%', containLabel: true },
  xAxis: { type: 'category', data: [], axisLabel: { color: '#9ca3af' } },
  yAxis: { type: 'value', min: 900, axisLabel: { color: '#9ca3af' }, splitLine: { lineStyle: { color: '#374151/50' } } },
  series: [{ name: 'Valor USD', type: 'line', data: [], itemStyle: { color: '#10b981' }, smooth: true, areaStyle: { color: 'rgba(16, 185, 129, 0.1)' } }]
});

const cargarPerfil = async () => {
  try {
    const respuesta = await fetch('/api/v1/profiles/usuarios/');
    const datos = await respuesta.json();
    if (datos.length > 0) miPerfil.value = datos[0];
  } catch (error) { console.error("Error al conectar el perfil:", error); }
};

const cargarDatosFinancieros = async () => {
  try {
    const respuesta = await fetch('/api/v1/analytics/api/finanzas/');
    const datosReales = await respuesta.json();
    chartOption.value.xAxis.data = datosReales.fechas;
    chartOption.value.series[0].data = datosReales.valores;
  } catch (error) { console.error("Error al conectar con Django:", error); }
};

const datosOportunidad = ref(null);
const cargarOportunidades = async () => {
  try {
    const respuesta = await fetch('/api/v1/analytics/api/oportunidad-etf/');
    const datos = await respuesta.json();
    datosOportunidad.value = datos;
  } catch (error) { console.error("Error al cargar las oportunidades de ETFs:", error); }
};

watch(datosOportunidad, async () => {
  await nextTick();
  if (observadorDeScroll) {
    document.querySelectorAll('.reveal').forEach((elemento) => { observadorDeScroll.observe(elemento); });
  }
});

// --- SIMULADOR DE JUBILACIÓN ---
const aporteMensual = ref(200); 
const anosProyeccion = ref(20); 
const tasaAnual = 0.10; 

const chartSimulador = ref({
  tooltip: {
    trigger: 'axis',
    formatter: function (params) {
      return `Año ${params[0].name}<br/>
              ${params[0].marker} Capital Invertido: $${params[0].value.toLocaleString('en-US')}<br/>
              ${params[1].marker} Rendimiento (Interés): $${params[1].value.toLocaleString('en-US')}<br/>
              <strong>Total Estimado: $${(params[0].value + params[1].value).toLocaleString('en-US')} USD</strong>`;
    }
  },
  legend: { data: ['Capital Invertido', 'Rendimiento (Interés)'], textStyle: { color: '#9ca3af' }, bottom: 0 },
  grid: { left: '5%', right: '5%', bottom: '15%', top: '10%', containLabel: true },
  xAxis: { type: 'category', boundaryGap: false, data: [], axisLabel: { color: '#9ca3af' } },
  yAxis: { type: 'value', axisLabel: { color: '#9ca3af' }, splitLine: { lineStyle: { color: '#374151/50' } } },
  series: [
    { name: 'Capital Invertido', type: 'line', stack: 'Total', areaStyle: { color: 'rgba(156, 163, 175, 0.2)' }, lineStyle: { color: '#9ca3af' }, itemStyle: { color: '#9ca3af' }, showSymbol: false, data: [] },
    { name: 'Rendimiento (Interés)', type: 'line', stack: 'Total', areaStyle: { color: 'rgba(16, 185, 129, 0.4)' }, lineStyle: { color: '#10b981' }, itemStyle: { color: '#10b981' }, showSymbol: false, data: [] }
  ]
});

const calcularProyeccion = () => {
  const categoriasAnos = [];
  const datosCapital = [];
  const datosInteres = [];
  let capitalAcumulado = 0;
  let totalAcumulado = 0;

  for (let i = 0; i <= anosProyeccion.value; i++) {
    categoriasAnos.push(i);
    if (i === 0) {
      datosCapital.push(0);
      datosInteres.push(0);
    } else {
      capitalAcumulado += (aporteMensual.value * 12);
      totalAcumulado = (totalAcumulado + (aporteMensual.value * 12)) * (1 + tasaAnual);
      datosCapital.push(Math.round(capitalAcumulado));
      datosInteres.push(Math.round(totalAcumulado - capitalAcumulado));
    }
  }
  chartSimulador.value.xAxis.data = categoriasAnos;
  chartSimulador.value.series[0].data = datosCapital;
  chartSimulador.value.series[1].data = datosInteres;
};

watch([aporteMensual, anosProyeccion], () => { calcularProyeccion(); });

// --- ARRANQUE DE LA VISTA ---
onMounted(() => {
  observadorDeScroll = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if (entrada.isIntersecting) entrada.target.classList.add('reveal-active');
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal').forEach((elemento) => { observadorDeScroll.observe(elemento); });

  cargarDatosFinancieros();
  cargarOportunidades();
  calcularProyeccion();
  cargarPerfil();
  cargarCategorias(); 
  cargarProyectos();
  
  timerMaquinaEscribir = setTimeout(escribir, 1000);
  timerGlitch = setTimeout(iniciarEfectoGlitch, 3500); 
});

onUnmounted(() => {
  clearTimeout(timerMaquinaEscribir);
  clearTimeout(timerGlitch);
  if (observadorDeScroll) observadorDeScroll.disconnect();
});
</script>

<template>
  <div class="flex flex-col w-full">
    
    <!-- SECCIÓN HERO -->
    <section id="inicio" class="flex flex-col items-center justify-center text-center px-4 relative min-h-[90vh]">
      <!-- SISTEMA SOLAR DE MEDALLAS FLOTANTES -->
      <div class="absolute top-24 left-[15%] md:left-1/4 animate-levitate-slow bg-white/5 backdrop-blur-md border border-emerald-500/30 px-4 py-2 rounded-2xl flex items-center gap-2 shadow-[0_0_15px_rgba(16,185,129,0.2)] reveal delay-300">
        <span class="text-emerald-400 font-bold text-sm">Vue 3</span>
      </div>
      <div class="absolute bottom-60 md:bottom-40 right-[15%] md:right-1/4 animate-levitate-fast bg-white/5 backdrop-blur-md border border-blue-500/30 px-4 py-2 rounded-2xl flex items-center gap-2 shadow-[0_0_15px_rgba(59,130,246,0.2)] reveal delay-500">
      </div>
      <div class="absolute top-40 right-[10%] md:right-1/3 animate-[levitate_6s_ease-in-out_infinite] opacity-40 bg-black/40 border border-white/5 px-3 py-1 rounded-xl flex items-center gap-2 scale-110 reveal delay-700">
        <span class="text-yellow-400 font-mono text-xs">Python</span>
      </div>
      <div class="absolute bottom-32 left-[10%] md:left-1/3 animate-[levitate_8s_ease-in-out_infinite] opacity-40 bg-black/40 border border-white/5 px-3 py-1 rounded-xl flex items-center gap-2 scale-95 reveal delay-[900ms]">
        <span class="text-cyan-400 font-mono text-xs">MySQL</span>
      </div>
      <div class="absolute bottom-32 left-[50%] md:left-1/8 animate-[levitate_8s_ease-in-out_infinite] opacity-40 bg-black/40 border border-white/5 px-3 py-1 rounded-xl flex items-center gap-2 scale-95 reveal delay-[900ms]">
        <span class="text-cyan-400 font-mono text-xs">Linux Server</span>
      </div>
      <div class="absolute top-24 right-[10%] md:right-1/6 animate-levitate-slow bg-white/5 backdrop-blur-md border border-emerald-500/30 px-4 py-2 rounded-2xl flex items-center gap-2 shadow-[0_0_15px_rgba(16,185,129,0.2)] reveal delay-300">
        <span class="text-emerald-400 font-bold text-sm">AWS</span>
      </div>

      <!-- AVATAR -->
      <div class="mb-2 reveal z-10 w-20 h-20 md:w-24 md:h-24 rounded-full bg-emerald-900/30 border border-emerald-500/50 overflow-hidden shadow-[0_0_20px_rgba(16,185,129,0.3)] flex items-center justify-center transform hover:scale-110 transition-transform duration-300">
        <img v-if="miPerfil.avatar_3d" :src="miPerfil.avatar_3d" alt="Avatar 3D" class="w-full h-full object-cover object-top" />
        <svg v-else class="w-10 h-10 text-emerald-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
      </div>

      <!-- TÍTULO MUTANTE -->
      <h1 class="text-5xl md:text-7xl lg:text-8xl font-black mb-6 tracking-tight reveal z-10 min-h-[120px] md:min-h-[150px] flex items-center justify-center">
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-500 drop-shadow-lg relative font-mono transition-all duration-300">
          {{ textoPrincipal }}
          <div class="absolute inset-0 bg-emerald-500/20 blur-[40px] -z-10"></div>
        </span>
      </h1>
      
      <!-- TITULAR CON MÁQUINA DE ESCRIBIR -->
      <div class="inline-flex items-center gap-3 mb-10 reveal delay-200 bg-white/5 px-6 py-2 rounded-full border border-white/10 backdrop-blur-sm h-14 min-w-[320px] justify-center">
        <svg class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M4 18h16a2 2 0 002-2V8a2 2 0 00-2-2H4a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
        <p class="text-lg md:text-xl text-gray-300 font-light">
          {{ textoActual }}<span class="animate-pulse text-emerald-400 font-black ml-1">_</span>
        </p>
      </div>
      
      <!-- BOTÓN PULSANTE -->
      <a href="#proyectos" class="reveal delay-300 relative group inline-flex">
        <span class="absolute inset-0 rounded-full bg-emerald-500/50 animate-ping opacity-75"></span>
        <span class="relative px-8 py-4 bg-emerald-500 text-gray-950 font-bold rounded-full hover:bg-emerald-400 transition-all shadow-[0_0_30px_rgba(16,185,129,0.3)] hover:shadow-[0_0_50px_rgba(16,185,129,0.6)] flex items-center gap-2 group-hover:-translate-y-1">
          Explorar mi trabajo
          <svg class="w-4 h-4 transform group-hover:rotate-90 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </span>
      </a>

      <!-- INDICADOR DE SCROLL -->
      <div class="absolute bottom-8 flex flex-col items-center gap-2 opacity-50 hover:opacity-100 transition-opacity cursor-default reveal delay-[1000ms]">
        <span class="text-xs font-mono uppercase tracking-[0.3em] text-gray-400">Descubre Más</span>
        <div class="w-px h-12 bg-gradient-to-b from-emerald-500 to-transparent"></div>
      </div>
    </section>

    <!-- SECCIÓN PROYECTOS -->
    <section id="proyectos" class="w-full px-6 py-24 z-10">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-4xl font-bold text-white mb-8 text-center tracking-tight reveal">Proyectos Destacados</h2>
        
        <div class="flex flex-wrap justify-center gap-4 mb-12 reveal">
          <button v-for="cat in categorias" :key="cat.id" @click="filtroActual = cat.name" :class="['px-6 py-2 rounded-full font-bold text-sm transition-all duration-300 border cursor-pointer', filtroActual === cat.name ? 'bg-emerald-500 text-gray-950 border-emerald-500 shadow-[0_0_15px_rgba(16,185,129,0.4)] transform scale-105' : 'bg-transparent text-gray-400 border-white/10 hover:border-emerald-500/50 hover:text-emerald-400']">
            {{ cat.name }}
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <article v-for="(proyecto, index) in proyectosFiltrados" :key="proyecto.id" class="reveal bg-white/5 backdrop-blur-xl p-6 rounded-3xl border border-white/10 hover:border-emerald-500/50 hover:bg-white/10 transition-all duration-300 group hover:-translate-y-2 hover:shadow-[0_10px_40px_rgba(16,185,129,0.1)] flex flex-col" :style="`transition-delay: ${index * 100}ms`">
            <div class="w-full h-48 mb-6 overflow-hidden rounded-2xl relative">
              <img :src="proyecto.image" :alt="proyecto.title" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500" />
              <span v-if="proyecto.featured" class="absolute top-3 right-3 bg-emerald-500 text-gray-950 text-xs font-bold px-3 py-1 rounded-full shadow-lg">Destacado</span>
            </div>
            <div class="mb-4">
              <span class="text-xs font-mono text-emerald-400 mb-2 block">{{ proyecto.category ? proyecto.category.name : 'Sin Categoría' }}</span>
              <h3 class="text-2xl font-bold text-white group-hover:text-emerald-400 transition-colors">{{ proyecto.title }}</h3>
            </div>
            <div class="flex flex-wrap gap-2 mb-4">
              <span v-for="tech in proyecto.technologies" :key="tech.id" class="inline-block px-3 py-1 bg-black/40 text-gray-300 rounded-full font-mono text-xs border border-white/5">{{ tech.name }}</span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed flex-grow">{{ proyecto.summary }}</p>
            <a v-if="proyecto.project_url" :href="proyecto.project_url" target="_blank" class="mt-6 inline-flex items-center gap-2 text-emerald-400 font-semibold hover:text-white transition-colors">
              Ver Proyecto <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </a>
          </article>
        </div>

        <!-- ... justo debajo del </div> que cierra el grid de proyectos ... -->
        
        <!-- BOTÓN: VER TODOS LOS PROYECTOS -->
        <div class="mt-16 text-center reveal">
          <router-link 
            to="/proyectos" 
            class="inline-flex items-center gap-3 px-8 py-4 bg-slate-900/50 border border-emerald-500/30 text-emerald-400 font-bold rounded-full hover:bg-emerald-500/10 hover:-translate-y-1 transition-all duration-300 group shadow-lg"
          >
            Ver todos mis proyectos
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
          </router-link>
        </div>

      </div>
    </section>

    <!-- SECCIÓN BI -->
    <section id="bi" class="w-full px-6 py-24 bg-black/40 border-y border-white/5 z-10">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-12 reveal max-w-4xl mx-auto">
          <h2 class="text-4xl font-bold text-white mb-4 tracking-tight">Inteligencia de Negocio</h2>
          <span class="inline-block px-4 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-full font-mono text-xs uppercase tracking-widest mb-6">Paneles de Control para Toma de Decisiones</span>
          <p class="text-gray-400 text-lg leading-relaxed mb-4"><strong>¿Por qué muestro estos datos financieros?</strong> Esta sección es una demostración en vivo del motor analítico que puedo construir para tu empresa. Utilicé APIs del mercado real como ejemplo para probar mi capacidad de extraer, transformar y graficar datos complejos en tiempo real.</p>
          <p class="text-gray-400 text-lg leading-relaxed">Imagina este mismo panel conectado a tu propia base de datos: podrías medir tendencias de ventas, controlar el flujo de tu inventario clínico, o visualizar qué insumos se consumen más en ciertos sectores para decidir estratégicamente dónde invertir tus recursos. Si necesitas que los datos de tu negocio hablen para tomar mejores decisiones, esta es la arquitectura que diseñaré para ti.</p>
        </div>

        <div class="mb-16 reveal delay-100" v-if="datosOportunidad">
          <div class="flex flex-col md:flex-row items-center justify-between mb-8 gap-4">
            <h3 class="text-2xl font-bold text-white tracking-tight">Radar de Oportunidades (ETFs)</h3>
            <div class="flex items-center gap-2 bg-slate-900/80 border border-slate-700 px-4 py-2 rounded-full shadow-inner">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span class="text-sm font-mono text-gray-300">Dólar Observado: <strong class="text-emerald-400">${{ datosOportunidad.dolar_hoy }} CLP</strong></span>
            </div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div v-for="etf in datosOportunidad.oportunidades" :key="etf.fondo" class="bg-white/5 backdrop-blur-xl p-6 rounded-3xl transition-all duration-300 group cursor-default" :class="etf.en_oferta ? 'border-2 border-emerald-500/50 shadow-[0_0_20px_rgba(16,185,129,0.15)] hover:-translate-y-2' : 'border border-white/10 hover:border-white/20 hover:-translate-y-1'">
              <div class="flex justify-between items-start mb-6">
                <h4 class="text-3xl font-black text-white group-hover:text-emerald-400 transition-colors">{{ etf.fondo }}</h4>
                <span class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest border text-center" :class="etf.en_oferta ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-red-500/10 text-red-400 border-red-500/30'">{{ etf.en_oferta ? 'Comprar Ahora' : 'Pausar Compra' }}</span>
              </div>
              <div class="space-y-2">
                <div class="flex justify-between items-center border-b border-white/5 pb-2"><span class="text-gray-400 text-sm">Precio USD:</span><span class="text-white font-mono font-medium">${{ etf.precio_usd }}</span></div>
                <div class="flex justify-between items-center pt-2"><span class="text-gray-400 text-sm">Costo Real CLP:</span><span class="text-emerald-300 font-mono font-bold">${{ etf.costo_clp.toLocaleString('es-CL') }}</span></div>
              </div>
            </div>
          </div>
          <div class="bg-slate-900/50 border border-slate-800 rounded-2xl p-5 flex items-start gap-4">
            <svg class="w-6 h-6 text-emerald-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <p class="text-sm text-gray-400 leading-relaxed"><strong class="text-gray-200">¿Cómo funciona este radar?</strong> Este algoritmo extrae en tiempo real el valor del dólar en Chile y el precio de cierre de la bolsa. Si el valor del activo en USD presenta una caída respecto a la jornada anterior, el sistema emite una señal de <strong>"Comprar Ahora"</strong>, indicando una ventana ideal para adquirir fracciones a menor costo.</p>
          </div>
        </div>
                
        <div class="reveal delay-200 bg-white/5 backdrop-blur-xl rounded-3xl border border-white/10 p-8 flex flex-col items-center justify-center w-full shadow-2xl relative overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-emerald-500/5 to-transparent pointer-events-none"></div>
          <h3 class="text-white font-semibold text-lg mb-6 w-full text-left flex items-center gap-3 relative z-10">
            <span class="relative flex h-3 w-3"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span><span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span></span>
            Live: Variación USD/CLP (7 días)
          </h3>
          <div class="w-full h-[300px] md:h-[400px] relative z-10"><v-chart :option="chartOption" autoresize /></div>
          <div class="bg-slate-900/50 border border-slate-800 rounded-2xl p-5 flex items-start gap-4 w-full mt-8 relative z-10 text-left">
            <svg class="w-6 h-6 text-blue-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <p class="text-sm text-gray-400 leading-relaxed"><strong class="text-gray-200">Tendencia del Dólar (Últimos 7 días):</strong> Visualización interactiva alimentada por la API de Mindicador. Evaluar la curva macroeconómica del tipo de cambio es un paso crítico en la estrategia de inversión; un dólar con tendencia a la baja reduce el costo real al adquirir instrumentos financieros en el extranjero.</p>
          </div>
        </div>

        <!-- SIMULADOR DE JUBILACIÓN -->
        <div class="mt-16 reveal delay-300 bg-slate-900/40 backdrop-blur-xl rounded-3xl border border-white/10 p-8 shadow-2xl relative overflow-hidden w-full">
          <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-8">
            <div class="flex-1"><h3 class="text-3xl font-bold text-white tracking-tight mb-2">Simulador de Patrimonio</h3><p class="text-gray-400">Analítica predictiva basada en el rendimiento histórico del S&P 500 (~10% anual).</p></div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 mb-10 bg-black/20 p-6 rounded-2xl border border-white/5">
            <div>
              <div class="flex justify-between items-center mb-4"><label class="text-sm font-semibold text-emerald-400 uppercase tracking-widest">Aporte Mensual</label><span class="text-2xl font-mono font-bold text-white">${{ aporteMensual }} USD</span></div>
              <input type="range" v-model="aporteMensual" min="50" max="2000" step="50" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-emerald-500 hover:accent-emerald-400 transition-all">
            </div>
            <div>
              <div class="flex justify-between items-center mb-4"><label class="text-sm font-semibold text-emerald-400 uppercase tracking-widest">Horizonte de Inversión</label><span class="text-2xl font-mono font-bold text-white">{{ anosProyeccion }} Años</span></div>
              <input type="range" v-model="anosProyeccion" min="5" max="40" step="1" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-emerald-500 hover:accent-emerald-400 transition-all">
            </div>
          </div>
          <div class="w-full h-[350px] md:h-[450px] relative z-10"><v-chart :option="chartSimulador" autoresize /></div>
        </div>
      </div>
    </section>

    <!-- SECCIÓN ACERCA DE MÍ -->
    <section id="sobre-mi" class="w-full px-6 py-24 z-10 mb-20">
      <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
        <div class="reveal">
          <h2 class="text-4xl font-bold text-white mb-6 tracking-tight">Sobre Mi</h2>
          <p class="text-gray-400 text-lg mb-4 leading-relaxed font-light whitespace-pre-line">{{ miPerfil.bio }}</p>
          <div class="mt-8 flex">
            <a :href="miPerfil.social_links?.find(link => link.platform.toLowerCase() === 'whatsapp')?.url || '#'" target="_blank" class="px-8 py-3 bg-emerald-500 text-gray-950 font-bold rounded-full hover:bg-emerald-400 transition-all shadow-[0_0_20px_rgba(16,185,129,0.3)] hover:shadow-[0_0_40px_rgba(16,185,129,0.6)] hover:-translate-y-1 inline-flex items-center gap-2">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.591 5.52 0 10.02-4.5 10.02-10.02 0-5.52-4.5-10.02-10.02-10.02-5.52 0-10.02 4.5-10.02 10.02 0 1.956.566 3.815 1.548 5.462l-1.05 3.845 3.847-1.05zm10.742-7.534c-.073-.117-.266-.191-.557-.336-.29-.145-1.724-.851-1.991-.948-.266-.097-.46-.146-.653.146-.194.292-.751.948-.921 1.142-.169.194-.339.218-.63.073-.29-.145-1.226-.452-2.335-1.443-.865-.771-1.448-1.724-1.618-2.016-.17-.292-.018-.45.128-.596.133-.133.292-.347.438-.521.146-.174.194-.296.292-.493.097-.197.049-.369-.025-.517-.073-.148-.653-1.572-.897-2.152-.234-.567-.472-.489-.653-.497-.168-.008-.361-.01-.555-.01-.194 0-.509.073-.775.364-.266.292-1.016.993-1.016 2.422s1.04 2.801 1.187 2.997c.146.197 2.051 3.134 4.965 4.394.693.298 1.233.477 1.654.613.696.22 1.332.189 1.832.114.557-.083 1.724-.705 1.967-1.385.244-.68.244-1.263.171-1.385-.073-.122-.266-.194-.557-.341z"/></svg>
              ¿Tienes un proyecto en mente?
              Hablemos!
            </a>
          </div>
        </div>
        <div class="flex justify-center relative reveal delay-200 mt-10 md:mt-0">
          <div class="absolute w-64 h-64 md:w-80 md:h-80 bg-emerald-500/20 rounded-full blur-[80px] z-0 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"></div>
          <div class="absolute w-72 h-72 md:w-96 md:h-96 rounded-full border border-dashed border-emerald-500/30 animate-[spin_20s_linear_infinite] z-0 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"></div>
          <div class="relative z-10 flex items-center justify-center w-72 h-72 md:w-96 md:h-96 overflow-visible">
            <img v-if="miPerfil.avatar" :src="miPerfil.avatar" alt="Patricio Riquelme Saez" class="w-full h-full object-contain drop-shadow-[0_10px_20px_rgba(16,185,129,0.15)] transform scale-125 -translate-y-4 hover:scale-[1.35] transition-transform duration-500" style="-webkit-mask-image: radial-gradient(circle at center, rgba(0,0,0,1) 50%, rgba(0,0,0,0) 75%); mask-image: radial-gradient(circle at center, rgba(0,0,0,1) 50%, rgba(0,0,0,0) 60%);" />
            <div v-else class="w-full h-full bg-white/5 backdrop-blur-md rounded-full border border-white/10 flex flex-col items-center justify-center text-center p-4">
              <svg class="w-12 h-12 text-gray-500 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span class="text-gray-500 text-xs font-mono block">Sube tu foto PNG <br> (Sin fondo) en Django</span>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>