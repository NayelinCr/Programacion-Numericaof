/* 🎀 Script principal del Portafolio de Nayelin 🎀
   🌸 Funcionalidad:
   - Botón "Volver arriba" con aparición suave.
   - Desplazamiento suave entre secciones.
   - Modo oscuro / claro (opcional).
*/

document.addEventListener("DOMContentLoaded", () => {
  const btnArriba = document.getElementById("btnArriba");
  const linksSuaves = document.querySelectorAll('a[href^="#"]');
  const btnTema = document.getElementById("btnTema");

  /* 🌷 Mostrar/ocultar botón al hacer scroll */
  window.addEventListener("scroll", () => {
    if (window.scrollY > 250) {
      btnArriba?.classList.add("mostrar");
    } else {
      btnArriba?.classList.remove("mostrar");
    }
  });

  /* 🌷 Función: volver arriba suavemente */
  btnArriba?.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  /* 🌸 Desplazamiento suave para enlaces internos */
  linksSuaves.forEach(link => {
    link.addEventListener("click", e => {
      const destino = document.querySelector(link.getAttribute("href"));
      if (destino) {
        e.preventDefault();
        destino.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  /* 🌙 Alternar tema oscuro/claro */
  btnTema?.addEventListener("click", () => {
    document.body.classList.toggle("oscuro");
    const esOscuro = document.body.classList.contains("oscuro");
    btnTema.innerHTML = esOscuro ? "🌙 Modo Claro" : "☀️ Modo Oscuro";
  });
});
