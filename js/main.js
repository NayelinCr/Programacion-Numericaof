document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector('header');
  const btnArriba = document.getElementById("btnArriba");
  const btnTema = document.getElementById("btnTema");
  
  // Scroll en el navbar
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    
    // Botón volver arriba
    if (window.scrollY > 300) {
      btnArriba.classList.add("mostrar");
    } else {
      btnArriba.classList.remove("mostrar");
    }
  });
  
  // Click en volver arriba
  btnArriba?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
  
  // Scroll suave para todos los enlaces internos
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const href = link.getAttribute("href");
      const target = document.querySelector(href);
      
      if (target) {
        // Calcular la posición con offset para el navbar
        const headerHeight = 80;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: "smooth"
        });
        
        // Actualizar enlaces activos
        document.querySelectorAll('.nav-links a').forEach(a => {
          a.classList.remove('active');
        });
        
        // Marcar como activo si es del navbar
        const navLink = document.querySelector(`.nav-links a[href="${href}"]`);
        if (navLink) {
          navLink.classList.add('active');
        }
      }
    });
  });
  
  // Toggle tema
  btnTema?.addEventListener("click", () => {
    const isLight = btnTema.innerHTML.includes("Claro");
    btnTema.innerHTML = isLight ? 
      "<span>☀️</span><span>Modo Claro</span>" : 
      "<span>🌙</span><span>Modo Oscuro</span>";
    localStorage.setItem("tema", isLight ? "oscuro" : "claro");
    // Aquí podrías agregar lógica para cambiar variables CSS si implementas modo claro real en el futuro
  });
  
  // Recuperar tema
  const temaGuardado = localStorage.getItem("tema");
  if (temaGuardado === "claro") {
    btnTema.innerHTML = "<span>🌙</span><span>Modo Oscuro</span>";
  }
  
  // Animaciones de scroll (Intersection Observer)
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { 
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  });
  
  document.querySelectorAll(".fade-up").forEach(el => {
    observer.observe(el);
  });
});
