<div id="wait-times-wrapper"></div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  const ciudad = "tijuana"; // Solo mostrar Tijuana
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
          const garitaContainer = document.createElement('div');
          garitaContainer.classList.add('garita-container');

          // Agregar el título de la garita
          const garitaHeader = document.createElement('div');
          garitaHeader.classList.add('garita-header');
          garitaHeader.innerHTML = `<h3 class="text-300">${garita}</h3>`;
          garitaContainer.appendChild(garitaHeader);

          // Contenedor de cruces
          const crucesWrapper = document.createElement('div');
          crucesWrapper.classList.add('cruce-Main-wrapper');

          data[garita].forEach(cruce => {
            const cruceContent = document.createElement('div');
            cruceContent.classList.add('cruce-content');

            // Asignar color según el JSON
            let color = "#A0A0A0"; // Default gray
            if (cruce.color === "red") color = "#FF3744";
            else if (cruce.color === "yellow") color = "#FFC803";
            else if (cruce.color === "green") color = "#00DD85";

            // Asignar icono según el tipo
            let iconoSvg = "";
            if (cruce.icono === "peatonal") {
              iconoSvg = `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#08161E" viewBox="0 0 256 256" style="opacity: 50%;">
                <path d="M120,48a32,32,0,1,1,32,32A32,32,0,0,1,120,48Zm88,88c-28.64,0-41.81-13.3-55.75-27.37-3.53-3.57-7.18-7.26-11-10.58-37-32.14-96.22,22.73-98.72,25.08a8,8,0,0,0,10.95,11.66A163.88,163.88,0,0,1,84,113c13.78-7.38,25.39-10.23,34.7-8.58L64.66,228.81a8,8,0,0,0,4.15,10.52A7.84,7.84,0,0,0,72,240a8,8,0,0,0,7.34-4.81l33.59-77.27L144,180.12V232a8,8,0,0,0,16,0V176a8,8,0,0,0-3.35-6.51l-37.2-26.57L132.88,112c2.64,2.44,5.26,5.07,8,7.84C155.05,134.19,172.69,152,208,152a8,8,0,0,0,0-16Z"></path>
              </svg>`;
            } else {
              iconoSvg = `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="#08161E" viewBox="0 0 256 256" style="opacity: 50%;">
                <path d="M240,104H229.2L201.42,41.5A16,16,0,0,0,186.8,32H69.2a16,16,0,0,0-14.62,9.5L26.8,104H16a8,8,0,0,0,0,16h8v80a16,16,0,0,0,16,16H64a16,16,0,0,0,16-16v-8h96v8a16,16,0,0,0,16,16h24a16,16,0,0,0,16-16V120h8a8,8,0,0,0,0-16ZM80,152H56a8,8,0,0,1,0-16H80a8,8,0,0,1,0,16Zm120,0H176a8,8,0,0,1,0-16h24a8,8,0,0,1,0,16ZM44.31,104,69.2,48H186.8l24.89,56Z"></path>
              </svg>`;
            }

            // Icono del cruce con el color de fondo asignado
            const cruceIcon = document.createElement('div');
            cruceIcon.classList.add('cruce-icon');
            cruceIcon.style.backgroundColor = color;
            cruceIcon.innerHTML = iconoSvg;
            cruceContent.appendChild(cruceIcon);

            // Detalles del cruce
            const cruceDetails = document.createElement('div');
            cruceDetails.classList.add('cruce-details');

            cruceDetails.innerHTML = `
              <div class="text-200">Tipo - ${cruce.tipo}</div>
              <div class="text-300"><b>Tiempo - ${cruce.tiempo}</b></div>
              <div class="text-200">Líneas - ${cruce.líneas_abiertas}</div>
            `;

            cruceContent.appendChild(cruceDetails);
            crucesWrapper.appendChild(cruceContent);
          });

          garitaContainer.appendChild(crucesWrapper);
          wrapper.appendChild(garitaContainer);
        }
      });
    })
    .catch(error => {
      wrapper.innerHTML += `<p>Error cargando información de ${ciudad}: ${error.message}</p>`;
    });
});
</script>