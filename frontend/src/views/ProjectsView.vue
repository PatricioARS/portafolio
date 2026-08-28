<template>
  <div class="pt-32 pb-20 px-6 max-w-7xl mx-auto min-h-screen reveal-active flex flex-col">
    
    <!-- ENCABEZADO -->
    <div class="text-center mb-16">
      <span class="inline-block px-4 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-full font-mono text-xs uppercase tracking-widest mb-4">
        Archivo Histórico
      </span>
      <h1 class="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-500 mb-6 tracking-tighter">
        Todos mis Proyectos
      </h1>
      <p class="text-gray-400 text-lg max-w-2xl mx-auto leading-relaxed">
        Explora la colección completa de mis desarrollos web, sistemas de gestión y configuraciones de servidores.
      </p>
    </div>

    <!-- FILTROS DE CATEGORÍA -->
    <div class="flex flex-wrap justify-center gap-4 mb-12">
      <button 
        v-for="cat in categorias" 
        :key="cat.id"
        @click="filtroActual = cat.name"
        :class="[
          'px-6 py-2 rounded-full font-bold text-sm transition-all duration-300 border cursor-pointer',
          filtroActual === cat.name 
            ? 'bg-emerald-500 text-gray-950 border-emerald-500 shadow-[0_0_15px_rgba(16,185,129,0.4)] transform scale-105' 
            : 'bg-transparent text-gray-400 border-white/10 hover:border-emerald-500/50 hover:text-emerald-400'
        ]"
      >
        {{ cat.name }}
      </button>
    </div>

    <!-- GRID DE PROYECTOS -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 flex-grow">
      <article 
        v-for="proyecto in proyectosFiltrados" 
        :key="proyecto.id"
        class="bg-white/5 backdrop-blur-xl p-6 rounded-3xl border border-white/10 hover:border-emerald-500/50 hover:bg-white/10 transition-all duration-300 group shadow-xl flex flex-col h-full"
      >
        <div class="w-full h-48 mb-6 overflow-hidden rounded-2xl relative">
          <img :src="proyecto.image" :alt="proyecto.title" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500" />
          <span v-if="proyecto.featured" class="absolute top-3 right-3 bg-emerald-500 text-gray-950 text-xs font-bold px-3 py-1 rounded-full shadow-lg">Destacado</span>
        </div>

        <div class="mb-4">
          <span class="text-xs font-mono text-emerald-400 mb-2 block">{{ proyecto.category ? proyecto.category.name : 'Sin Categoría' }}</span>
          <h3 class="text-2xl font-bold text-white group-hover:text-emerald-400 transition-colors">{{ proyecto.title }}</h3>
        </div>
        
        <div class="flex flex-wrap gap-2 mb-4">
          <span v-for="tech in proyecto.technologies" :key="tech.id" class="inline-block px-3 py-1 bg-black/40 text-gray-300 rounded-full font-mono text-xs border border-white/5">
            {{ tech.name }}
          </span>
        </div>
        
        <p class="text-gray-400 text-sm leading-relaxed flex-grow">{{ proyecto.summary }}</p>

        <a v-if="proyecto.project_url" :href="proyecto.project_url" target="_blank" class="mt-6 inline-flex items-center gap-2 text-emerald-400 font-semibold hover:text-white transition-colors">
          Ver Proyecto 
          <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </article>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const misProyectos = ref([]);
const categorias = ref([{ id: 0, name: 'Todos' }]);
const filtroActual = ref('Todos'); 

const cargarCategorias = async () => {
  try {
    const respuesta = await fetch('http://127.0.0.1:8000/api/v1/portafolio/categorias/');
    const datos = await respuesta.json();
    categorias.value = [{ id: 0, name: 'Todos' }, ...datos];
  } catch (error) { console.error("Error al cargar categorías:", error); }
};

const cargarProyectos = async () => {
  try {
    const respuesta = await fetch('http://127.0.0.1:8000/api/v1/portafolio/proyectos/');
    const datos = await respuesta.json();
    misProyectos.value = datos;
  } catch (error) { console.error("Error al cargar los proyectos:", error); }
};

const proyectosFiltrados = computed(() => {
  if (filtroActual.value === 'Todos') return misProyectos.value; 
  return misProyectos.value.filter(proyecto => proyecto.category && proyecto.category.name === filtroActual.value);
});

onMounted(() => {
  cargarCategorias(); 
  cargarProyectos();
});
</script>