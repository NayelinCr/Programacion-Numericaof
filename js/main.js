/* 🎀 Script principal del Portafolio de Nayelin (versión mejorada)
   ✨ Funcionalidad:
   - Botón "Volver arriba" animado y visible según el desplazamiento.
   - Desplazamiento suave entre secciones.
   - Modo oscuro / claro con almacenamiento de preferencia en localStorage.
   - Animaciones sutiles al cargar elementos.
*/

document.addEventListener("DOMContentLoaded", () => {
  const btnArriba = document.getElementById("btnArriba");
  const linksSuaves = document.querySelectorAll('a[href^="#"]');
  const btnTema = document.getElementById("btnTema");

  /* 🌙 Recuperar tema guardado */
  const temaGuardado = localStorage.getItem("tema");
  if (temaGuardado === "oscuro") {
    document.body.classList.add("oscuro");
    if (btnTema) btnTema.innerHTML = "🌙 Modo Claro";
  }

  /* 🌸 Mostrar/ocultar botón "Volver arriba" con animación */
  window.addEventListener("scroll", () => {
    if (window.scrollY > 250) {
      btnArriba?.classList.add("mostrar");
    } else {
      btnArriba?.classList.remove("mostrar");
    }
  });

  /* 🌷 Acción del botón "Volver arriba" */
  btnArriba?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* 💫 Desplazamiento suave entre secciones */
  linksSuaves.forEach(link => {
    link.addEventListener("click", e => {
      const destino = document.querySelector(link.getAttribute("href"));
      if (destino) {
        e.preventDefault();
        destino.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  /* 🌗 Alternar entre modo oscuro y claro */
  btnTema?.addEventListener("click", () => {
    document.body.classList.toggle("oscuro");
    const esOscuro = document.body.classList.contains("oscuro");

    btnTema.innerHTML = esOscuro ? "🌙 Modo Claro" : "☀️ Modo Oscuro";

    // Guardar preferencia
    localStorage.setItem("tema", esOscuro ? "oscuro" : "claro");

    // Pequeño efecto visual
    btnTema.animate([{ transform: "scale(1.1)" }, { transform: "scale(1)" }], {
      duration: 300,
      easing: "ease-out",
    });
  });

  /* 🪄 Animar contenido al cargar */
  const contenido = document.querySelector(".content");
  if (contenido) {
    contenido.style.opacity = 0;
    contenido.style.transform = "translateY(20px)";
    setTimeout(() => {
      contenido.style.transition = "all 0.8s ease-out";
      contenido.style.opacity = 1;
      contenido.style.transform = "translateY(0)";
    }, 300);
  }
});

