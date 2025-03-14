
<script>
<div id="wait-times-wrapper"></div>


document.addEventListener('DOMContentLoaded', () => {
  const ciudad = "tijuana"; // Solo mostrar Tijuana
  const wrapper = document.getElementById('wait-times-wrapper'); // ID corregido
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

            // Definir el ícono según el tipo de cruce
            let iconoUrl = "";
            if (cruce.tipo.toLowerCase().includes("peatonal") || cruce.tipo.toLowerCase().includes("pedwest")) {
            iconoUrl = "https://cdn-icons-png.flaticon.com/512/3448/3448609.png"; // Ícono de peatón
              } else {
            iconoUrl = "https://cdn-icons-png.flaticon.com/512/744/744465.png"; // Ícono de auto
            }


            // Icono del cruce
            const cruceIcon = document.createElement('div');
            cruceIcon.classList.add('cruce-icon');
            cruceIcon.innerHTML = `<img src="${iconoUrl}" alt="icono-cruce" width="32">`;
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