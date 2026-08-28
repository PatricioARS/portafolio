<template>
  <div class="pt-32 pb-20 px-6 max-w-7xl mx-auto min-h-[80vh] reveal-active">
    
    <!-- ENCABEZADO DE LA SECCIÓN -->
    <div class="text-center mb-16">
      <span class="inline-block px-4 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-full font-mono text-xs uppercase tracking-widest mb-4">
        Analisis y ciencia de datos
      </span>
      <h1 class="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-500 mb-6 tracking-tighter">
        Laboratorio de Datos
      </h1>
      <p class="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
        Exploración de datasets complejos, limpieza de datos y visualización de tendencias utilizando ecosistemas de Python para la toma de decisiones estratégicas.
      </p>
    </div>

    <!-- GRID DE CUADERNOS (NOTEBOOKS) -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      
      <!-- TARJETA 1: Análisis de Netflix -->
      <article class="bg-slate-900/40 border border-slate-800 rounded-3xl p-8 hover:border-emerald-500/50 transition-all duration-300 hover:-translate-y-2 cursor-pointer group shadow-xl flex flex-col h-full">
        <div class="flex items-center gap-4 mb-6">
          <div class="p-3 bg-red-500/10 rounded-xl group-hover:scale-110 transition-transform">
            <svg class="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
          </div>
          <h3 class="text-2xl font-bold text-white group-hover:text-emerald-400 transition-colors">Tendencias en Netflix</h3>
        </div>
        
        <p class="text-gray-400 mb-8 flex-grow leading-relaxed">
          Análisis exploratorio (EDA) de los géneros más consumidos a nivel global. Extracción y limpieza de un dataset público de Kaggle para identificar patrones de visualización y comportamiento de usuarios.
        </p>
        
        <div class="flex flex-wrap gap-2 mb-6">
          <span class="px-3 py-1 bg-black/50 text-gray-300 rounded-full text-xs font-mono border border-slate-700">Python</span>
          <span class="px-3 py-1 bg-black/50 text-gray-300 rounded-full text-xs font-mono border border-slate-700">Pandas</span>
          <span class="px-3 py-1 bg-black/50 text-gray-300 rounded-full text-xs font-mono border border-slate-700">Matplotlib</span>
        </div>

        <div class="w-full h-px bg-slate-800 mb-6"></div>

        <span class="inline-flex items-center gap-2 text-sm text-emerald-400 font-semibold group-hover:text-white transition-colors">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          En desarrollo...
        </span>
      </article>

      <!-- TARJETA 2: Espacio para futuro proyecto -->
      <article class="bg-slate-900/20 border border-slate-800/50 border-dashed rounded-3xl p-8 flex flex-col items-center justify-center text-center h-full min-h-[350px]">
         <svg class="w-12 h-12 text-slate-700 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
         <h3 class="text-xl font-bold text-slate-500 mb-2">Próximo Análisis</h3>
         <p class="text-slate-600 text-sm">Nuevo notebook de Google Colab en preparación.</p>
      </article>

    </div>
  </div>
</template>

<script setup>
// Aquí, en el futuro, haremos las llamadas a la API de Django para traer tus análisis reales
</script>