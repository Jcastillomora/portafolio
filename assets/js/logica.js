//JavaScript para proveer las funcionalidades de la pagina web

//Constantes para acceder a los elementos HTML
const select = document.getElementById('digimon-select');
const digimonImg = document.getElementById('digimon-img');
const digimonName = document.getElementById('digimon-name');
const digimonLevel = document.getElementById('digimon-level');
const audio = document.querySelector('audio');
          audio.currentTime = 25;
          audio.play();

//Cargar los digimons en el select desde la API
fetch('https://digimon-api.vercel.app/api/digimon')
  .then(response => response.json())
  .then(data => {
    data.forEach(digimon => {
      const option = document.createElement('option');
      option.text = digimon.name;
      option.value = digimon.name;
      select.add(option);
    });
  });

//Mostrar la informacion del digimon seleccionado desde la API
select.addEventListener('change', () => {
  const selectedDigimon = select.value;
  
  fetch(`https://digimon-api.vercel.app/api/digimon/name/${selectedDigimon}`)
    .then(response => response.json())
    .then(data => {
      digimonImg.src = data[0].img;
      digimonName.textContent = data[0].name;
      digimonLevel.textContent = `Nivel: ${data[0].level}`;
    });
});

//Ejemplos de DOM con javascript
//Seleccionar el elemento HTML h5
const h5 = document.querySelector('h5'); 

//Agregar un evento cuando se hace pasa el mouse sobre el elemento
h5.addEventListener('mouseover', () => { 
  h5.style.backgroundColor = '#3b2f2f';
  h5.style.color = '#00ff00';
  h5.style.animationDuration = '2s';
  h5.style.animationName = 'animacion1';
  h5.style.animationIterationCount = 'infinite';
});

//Agergar un evento cuando se quita el mouse del elemento
h5.addEventListener('mouseout', () => { 
  h5.style.backgroundColor = 'grey';
  h5.style.color = 'white';
});

//Ejemplo de DOM con javascript, mostrar mensaje al pasar el mouse sobre la imagen
function mostrarMensaje(event) {
  var mensaje = document.getElementById("mensaje");
  mensaje.style.display = "block";
  mensaje.style.position = "sticky";
  mensaje.innerHTML = "Esta es la imagen de un Digimon";
}

//Ejemplo de DOM con javascript, ocultar mensaje al quitar el mouse sobre la imagen
function ocultarMensaje() {
  var mensaje = document.getElementById("mensaje");
  mensaje.style.display = "none";
}