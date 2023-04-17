const form = document.querySelector('#task-form');
const input1 = document.querySelector('#country');
const input2 = document.querySelector('#city');
const input3 = document.querySelector('#daytrip');
const insert = document.querySelector('#collection');


loadEventlisteners();
    function loadEventlisteners() {
    form.addEventListener('submit', addList);
    }
function addList(e) {

    if(input1.value === '' || input2.value === '' || input3.value === '' ) {
        alert('select the country and city');
    }
    if (input3.value === 'half-day') {
        while( insert.firstChild ){
            insert.removeChild(insert.firstChild);
          }
        listPlaces("sac", "sanjose", "https://youtube.com/embed/_rbcG060frQ", "1");
        listPlaces("san", "Sacramanto", "https://youtube.com/embed/RJgPdNmfYaI", "2");
        listPlaces("davis", "Paicines", "https://www.youtube.com/embed/TjV3tPKzx70", "2");
     }
     if (input3.value === 'full-day') {
        while( insert.firstChild ){
            insert.removeChild(insert.firstChild);
          }
         listPlaces("san", "Lake Tahoe", "https://youtube.com/embed/_rbcG060frQ", "4");
         listPlaces("sac", "Yosemite", "https://www.youtube.com/embed/0Nbp7nNwOJ4", "4");
     }
    e.preventDefault();
}

function listPlaces(look, city, url, hours){   
    const li1 = document.createElement('li');
    li1.className = 'collection-item';
    li1.innerHTML = `<div class="row ${look}"><div class="col-10"><h1>${city}</h1><iframe id="video"src="${url}"></iframe></div><div class="col">${hours}  hrs</div></div>`
    li1.setAttribute("class", "click-btn");	
    li1.setAttribute ('style', 'display: block;');
    insert.appendChild(li1);
    }

         