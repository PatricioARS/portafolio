<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// --- SENSORES DE PARALLAX (Global) ---
const mouseX = ref(0);
const mouseY = ref(0);

const rastrearRaton = (evento) => {
  mouseX.value = (evento.clientX / window.innerWidth - 0.5) * 2;
  mouseY.value = (evento.clientY / window.innerHeight - 0.5) * 2;
};

// --- ANIMACIÓN DEL LOGO (Global) ---
const logoState = ref(0)
let logoInterval = null

// --- SENSOR DE BOTÓN Y MENÚ MÓVIL (Global) ---
const mostrarBotonSubir = ref(false);
const menuAbierto = ref(false);

const vigilarScroll = () => {
  mostrarBotonSubir.value = window.scrollY > 300;
};

const volverArriba = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

onMounted(() => {
  logoInterval = setInterval(() => {
    logoState.value = (logoState.value + 1) % 3
  }, 3500) 
  
  window.addEventListener('mousemove', rastrearRaton);
  window.addEventListener('scroll', vigilarScroll);
});

onUnmounted(() => {
  if (logoInterval) clearInterval(logoInterval);
  window.removeEventListener('mousemove', rastrearRaton);
  window.removeEventListener('scroll', vigilarScroll);
});
</script>

<template>
  <div class="min-h-screen bg-[#0B0F19] flex flex-col font-sans relative overflow-hidden text-gray-200">
    
    <!-- FONDO TECNOLÓGICO -->
    <div class="absolute inset-0 bg-grid opacity-40 pointer-events-none z-0"></div>
    <div class="fixed inset-0 z-0 flex items-center justify-center overflow-hidden pointer-events-none select-none opacity-20 bg-mask-radial">
      <pre class="font-mono text-emerald-400 text-xs md:text-sm leading-loose tracking-widest text-center">
def obtener_datos_financieros(request):
    url = 'https://mindicador.cl/api/dolar'
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    ultimos_dias = datos['serie'][:7]
    ultimos_dias.reverse() 
    
    dias = [dia['fecha'][8:10] + "-" + dia['fecha'][5:7] for dia in ultimos_dias]
    valores = [dia['valor'] for dia in ultimos_dias]
        
    return JsonResponse({'fechas': dias, 'valores': valores})
    
# Architecture: Django + Vue 3 
# Developer: Patricio Riquelme Saez
# Status: System Online
      </pre>
    </div>

    <!-- EFECTO GLOW CON PARALLAX 3D -->
    <div class="fixed top-0 left-1/4 w-96 h-96 bg-emerald-500/20 rounded-full blur-[120px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${mouseX * 40}px, ${mouseY * 40}px)` }"></div>
    <div class="fixed bottom-1/4 right-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-[120px] pointer-events-none transition-transform duration-700 ease-out z-0" :style="{ transform: `translate(${mouseX * -60}px, ${mouseY * -60}px)` }"></div>

    <!-- BARRA DE NAVEGACIÓN -->
    <nav class="w-full p-6 flex justify-between items-center z-50 sticky top-0 bg-[#0B0F19]/80 backdrop-blur-md border-b border-white/5 shadow-lg">
      <div class="flex items-center text-2xl font-black tracking-tighter select-none font-mono cursor-pointer relative z-50">
        <span class="text-emerald-400">P</span>
        <span class="inline-flex overflow-hidden transition-all duration-700 ease-in-out text-emerald-400" :class="{'max-w-[120px] opacity-100': logoState === 2, 'max-w-[20px] opacity-100': logoState === 1, 'max-w-0 opacity-0': logoState === 0}">
          {{ logoState === 1 ? 'o' : 'atricio' }}
        </span>
        <span class="text-slate-100">R</span>
        <span class="inline-flex overflow-hidden transition-all duration-700 ease-in-out text-slate-100" :class="{'max-w-[150px] opacity-100': logoState === 2 || logoState === 1, 'max-w-0 opacity-0': logoState === 0}">
          {{ logoState === 1 ? 'tafolio' : 'iquelme' }}
        </span>
        <span class="text-emerald-400 transition-opacity duration-500" :class="logoState === 0 ? 'opacity-100' : 'opacity-0'">.</span>
      </div>
      
      <!-- MENÚ DE ESCRITORIO CON VUE ROUTER Y ANCLAS -->
      <ul class="hidden md:flex space-x-8 text-gray-400 font-medium text-sm tracking-wide items-center">
        <li><router-link to="/" class="hover:text-emerald-400 transition-colors">Inicio</router-link></li>
        
        <!-- AQUÍ ESTÁ EL CAMBIO: Ahora Proyectos es una ruta SPA -->
        <li><router-link to="/proyectos" class="px-4 py-1.5 border border-emerald-500/30 text-emerald-400 rounded-full hover:bg-emerald-500/10 transition-all font-bold">Proyectos</router-link></li>
        
        <li>
          <!-- Botón resaltado del Lab de Datos -->
          <router-link to="/data-analysis" class="px-4 py-1.5 border border-emerald-500/30 text-emerald-400 rounded-full hover:bg-emerald-500/10 transition-all font-bold">
            Lab de Datos
          </router-link>
        </li>

        <li><a href="/#sobre-mi" class="px-4 py-1.5 border border-emerald-500/30 text-emerald-400 rounded-full hover:bg-emerald-500/10 transition-all font-bold">Sobre Mí</a></li>
             
      </ul>

      <!-- BOTÓN HAMBURGUESA -->
      <button @click="menuAbierto = !menuAbierto" class="md:hidden text-gray-300 hover:text-emerald-400 z-50 relative cursor-pointer" aria-label="Alternar menú">
        <svg v-if="!menuAbierto" class="w-8 h-8 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        <svg v-else class="w-8 h-8 transition-transform rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>

      <!-- MENÚ MÓVIL DESPLEGABLE -->
      <div :class="menuAbierto ? 'translate-y-0 opacity-100' : '-translate-y-full opacity-0 pointer-events-none'" class="fixed top-0 left-0 w-full h-screen bg-[#0B0F19]/95 backdrop-blur-xl flex flex-col items-center justify-center space-y-8 transition-all duration-500 ease-in-out md:hidden z-40">
        <router-link @click="menuAbierto = false" to="/" class="text-3xl font-bold text-white hover:text-emerald-400 transition-colors">Inicio</router-link>
        
        <!-- AQUÍ TAMBIÉN ESTÁ EL CAMBIO PARA MÓVILES -->
        <router-link @click="menuAbierto = false" to="/proyectos" class="text-3xl font-bold text-emerald-400 hover:text-emerald-300 transition-colors mt-4">Proyectos</router-link>
        <router-link @click="menuAbierto = false" to="/data-analysis" class="text-3xl font-bold text-emerald-400 hover:text-emerald-300 transition-colors mt-4">Lab de Datos</router-link>

        <a @click="menuAbierto = false" href="#sobre-mi" class="text-3xl font-bold text-emerald-400 hover:text-emerald-300 transition-colors mt-4">Sobre Mí</a>
      </div>
    </nav>

    <!-- EL MAGO DEL ENRUTAMIENTO: Aquí se inyecta HomeView o DataAnalysisView -->
    <main class="flex-grow flex flex-col relative z-10 w-full">
      <router-view />
    </main>

    <!-- FOOTER -->
    <footer class="w-full py-12 text-center border-t border-white/5 z-10 bg-[#0B0F19]">
      <div class="flex justify-center space-x-8 mb-8">
        <a href="https://wa.me/56996900714" target="_blank" class="text-gray-400 hover:text-emerald-400 transition-colors"><svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.591 5.52 0 10.02-4.5 10.02-10.02 0-5.52-4.5-10.02-10.02-10.02-5.52 0-10.02 4.5-10.02 10.02 0 1.956.566 3.815 1.548 5.462l-1.05 3.845 3.847-1.05zm10.742-7.534c-.073-.117-.266-.191-.557-.336-.29-.145-1.724-.851-1.991-.948-.266-.097-.46-.146-.653.146-.194.292-.751.948-.921 1.142-.169.194-.339.218-.63.073-.29-.145-1.226-.452-2.335-1.443-.865-.771-1.448-1.724-1.618-2.016-.17-.292-.018-.45.128-.596.133-.133.292-.347.438-.521.146-.174.194-.296.292-.493.097-.197.049-.369-.025-.517-.073-.148-.653-1.572-.897-2.152-.234-.567-.472-.489-.653-.497-.168-.008-.361-.01-.555-.01-.194 0-.509.073-.775.364-.266.292-1.016.993-1.016 2.422s1.04 2.801 1.187 2.997c.146.197 2.051 3.134 4.965 4.394.693.298 1.233.477 1.654.613.696.22 1.332.189 1.832.114.557-.083 1.724-.705 1.967-1.385.244-.68.244-1.263.171-1.385-.073-.122-.266-.194-.557-.341z"/></svg></a>
        <a href="https://instagram.com/patricioars/" target="_blank" class="text-gray-400 hover:text-emerald-400 transition-colors"><svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 1.15.053 1.77.25 2.184.414.553.215.948.473 1.36.886.413.413.67.808.886 1.36.164.435.361 1.035.414 2.184.059 1.266.07 1.646.07 4.85s-.012 3.584-.07 4.85c-.053 1.15-.25 1.77-.414 2.184-.215.553-.473.948-.886 1.36-.413.413-.808.67-1.36.886-.435.164-1.035.361-2.184.414-1.266.059-1.646.07-4.85.07s-3.584-.012-4.85-.07c-1.15-.053-1.77-.25-2.184-.414-.553-.215-.948-.473-1.36-.886-.413-.413-.67-.808-.886-1.36-.164-.435-.361-1.035-.414-2.184-.059-1.266-.07-1.646-.07-4.85s.012-3.584.07-4.85c.053-1.15.25-1.77.414-2.184.215-.553.473-.948.886-1.36.413-.413.808-.67 1.36-.886.435-.164 1.035-.361 2.184-.414 1.266-.059 1.646-.07 4.85-.07m0-2.163c-3.259 0-3.667.014-4.947.072-1.277.058-2.15.253-2.915.553-.79.306-1.458.718-2.126 1.386-.668.668-1.08 1.335-1.386 2.126-.3.765-.495 1.638-.553 2.915-.059 1.28-.072 1.688-.072 4.947s.014 3.667.072 4.947c.058 1.277.253 2.15.553 2.915.306.79.718 1.458 1.386 2.126.668.668 1.335 1.08 2.126 1.386.765.3 1.638.495 2.915.553 1.28.059 1.688.072 4.947.072s3.667-.014 4.947-.072c1.277-.058 2.15-.253 2.915-.553.79-.306 1.458-.718 2.126-1.386.668-.668 1.08-1.335 1.386-2.126.3-.765.495-1.638.553-2.915.059-1.28.072-1.688.072-4.947s-.014-3.667-.072-4.947c-.058-1.277-.253-2.15-.553-2.915-.306-.79-.718-1.458-1.386-2.126-.668-.668-1.335-1.08-2.126-1.386-.765-.3-1.638-.495-2.915-.553-1.28-.059-1.688-.072-4.947-.072z"/><path d="M12 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zm0 10.162a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg></a>
        <a href="https://github.com/tu_usuario" target="_blank" class="text-gray-400 hover:text-emerald-400 transition-colors"><svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>
      </div>
      <p class="text-gray-600 text-sm font-light">© 2026 Patricio Riquelme Saez. Todos los derechos reservados. | Desarrollado con Django & Vue.</p>
    </footer>

    <!-- BOTÓN VOLVER ARRIBA -->
    <button v-show="mostrarBotonSubir" @click="volverArriba" class="fixed bottom-8 right-8 z-50 p-3 bg-emerald-500 text-gray-950 rounded-full shadow-[0_0_20px_rgba(16,185,129,0.5)] hover:bg-emerald-400 hover:-translate-y-2 transition-all duration-300 group" aria-label="Volver arriba">
      <svg class="w-6 h-6 transform group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path></svg>
    </button>
  </div>
</template>

<style>
/* Conservamos todo tu estilo global de animaciones en App.vue */
html { scroll-behavior: smooth; }
.bg-grid { background-size: 40px 40px; background-image: linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px); mask-image: radial-gradient(circle at center, black 30%, transparent 80%); -webkit-mask-image: radial-gradient(circle at center, black 30%, transparent 80%); }
.bg-mask-radial { mask-image: radial-gradient(ellipse at center, black 10%, transparent 60%); -webkit-mask-image: radial-gradient(ellipse at center, black 10%, transparent 60%); }
.reveal { opacity: 0; transform: translateY(40px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
.reveal-active { opacity: 1; transform: translateY(0); }
.delay-100 { transition-delay: 100ms; }
.delay-200 { transition-delay: 200ms; }
.delay-300 { transition-delay: 300ms; }
.delay-500 { transition-delay: 500ms; }
@keyframes levitate { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
.animate-levitate-slow { animation: levitate 6s ease-in-out infinite; }
.animate-levitate-fast { animation: levitate 4s ease-in-out infinite; }
</style>