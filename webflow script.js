<div id="wait-times-wrapper"></div>


<script>
document.addEventListener('DOMContentLoaded', () => {

  
  const ciudad = "tijuana"; 
  const URL = `https://bordify.com/?city=${ciudad}`; // Ahora usa la variable ciudad
  const wrapper = document.getElementById('wait-times-wrapper'); 
  const jsonUrl = `https://brian-madmath.github.io/border-wait-times/wait-times-${ciudad}.json`;



  fetch(jsonUrl)
    .then(response => {
      if (!response.ok) throw new Error(`No se pudo cargar JSON de ${ciudad}`);
      return response.json();
    })
    .then(data => {
      Object.keys(data).forEach(garita => {
        if (garita !== "Ultima_actualizacion") {
          const garitaContainer = document.createElement('a');
          garitaContainer.href = URL;
          garitaContainer.classList.add('garita-container');

          const garitaHeader = document.createElement('div');
          garitaHeader.classList.add('garita-header');

          const garitaTitle = document.createElement('div');
          garitaTitle.classList.add("text-300", "medium");
          garitaTitle.textContent = garita;

          garitaHeader.appendChild(garitaTitle);
          garitaContainer.appendChild(garitaHeader);

          const crucesWrapper = document.createElement('div');
          crucesWrapper.classList.add('cruce-main-wrapper');

          data[garita].forEach(cruce => {
            const cruceContent = document.createElement('div');
            cruceContent.classList.add('cruce-content');

            let color = "#A0A0A0";
            if (cruce.color === "red") color = "#FF3744";
            else if (cruce.color === "yellow") color = "#FFC803";
            else if (cruce.color === "green") color = "#00DD85";

            let iconoSvg = `<div class="svg-icon-32"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#08161E" viewBox="0 0 256 256" style="opacity: 50%;">
                <path d="M240,104H229.2L201.42,41.5A16,16,0,0,0,186.8,32H69.2a16,16,0,0,0-14.62,9.5L26.8,104H16a8,8,0,0,0,0,16h8v80a16,16,0,0,0,16,16H64a16,16,0,0,0,16-16v-8h96v8a16,16,0,0,0,16,16h24a16,16,0,0,0,16-16V120h8a8,8,0,0,0,0-16ZM80,152H56a8,8,0,0,1,0-16H80a8,8,0,0,1,0,16Zm120,0H176a8,8,0,0,1,0-16h24a8,8,0,0,1,0,16ZM44.31,104,69.2,48H186.8l24.89,56Z"></path>
              </svg></div>`;

            const cruceIcon = document.createElement('div');
            cruceIcon.classList.add('cruce-icon');
            cruceIcon.style.backgroundColor = color;
            cruceIcon.innerHTML = iconoSvg;
            cruceContent.appendChild(cruceIcon);

            const cruceDetails = document.createElement('div');
            cruceDetails.classList.add('cruce-details');

            cruceDetails.innerHTML = `
              <div class="text-200">${cruce.tipo}</div>
              <div class="text-300 medium">${cruce.tiempo}</div>
              <div class="text-200">${cruce.líneas_abiertas}</div>
            `;

            cruceContent.appendChild(cruceDetails);
            crucesWrapper.appendChild(cruceContent);
          });

          garitaContainer.appendChild(crucesWrapper);
          wrapper.appendChild(garitaContainer);
        }
      });

      // 🔹 Obtener la última actualización y mostrar hace cuánto tiempo fue
      if (data["Ultima_actualizacion"]) {
        const ultimaActualizacion = new Date(data["Ultima_actualizacion"]); // Convertir string a Date
        const ahora = new Date(); // Fecha actual
        const diferencia = Math.floor((ahora - ultimaActualizacion) / 1000); // Diferencia en segundos

        let tiempoTexto = "Actualizado hace ";
        if (diferencia < 60) {
          tiempoTexto += `${diferencia} segundos`;
        } else if (diferencia < 3600) {
          tiempoTexto += `${Math.floor(diferencia / 60)} minutos`;
        } else if (diferencia < 86400) {
          tiempoTexto += `${Math.floor(diferencia / 3600)} horas`;
        } else {
          tiempoTexto += `${Math.floor(diferencia / 86400)} días`;
        }

        const actualizacionTexto = document.createElement('div');
        actualizacionTexto.classList.add('text-300', 'actualizacion-texto');
        actualizacionTexto.textContent = tiempoTexto + ".";
        actualizacionTexto.style.textAlign = "center"; // Centrar texto
        actualizacionTexto.style.display = "block"; 
        actualizacionTexto.style.marginTop = "10px"; 
        
        wrapper.appendChild(actualizacionTexto);
        

        wrapper.appendChild(actualizacionTexto);
      }
    })
    .catch(error => {
      wrapper.innerHTML += `<p>Error cargando información de ${ciudad}: ${error.message}</p>`;
    });
});
</script>

<style> 
a {
  text-decoration: none; /* Elimina el subrayado */
  color: inherit; /* Hereda el color del texto del elemento padre */
}

a:hover, a:focus {
  text-decoration: none;
  color: inherit;
}
</style>