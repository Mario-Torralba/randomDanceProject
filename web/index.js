const listaGrupos = document.getElementById("listaGrupos");
const eleccionGrupo = document.getElementById("eleccionGrupo")
const eleccionCancion = document.getElementById("eleccionCancion")
const main = document.getElementById("main")
var grupos = document.querySelectorAll('.grupo')

document.body.addEventListener("load", initComponents());

function initComponents() {

  let inputGrupo = document.getElementById("inputGrupo");

  findGroup(inputGrupo.value)


  inputGrupo.addEventListener("change", () => {
    findGroup(inputGrupo.value);
  });
}

function findGroup(grupo) {
  $.ajax({
    url: "Controller",
    data: {
      ACTION: "USUARIO.FINDALL",
      GRUPO: grupo,
    },
    dataType: "json",
    success: function (responseText) {
      console.log(responseText);
      showGroups(responseText)
    },
  });
}

function showGroups(response) {
  listaGrupos.innerHTML = "";

    if(response.length>10){

      for (let index = 0; index < 10; index++) {
        let grupo = document.createElement("div");
        grupo.className = "grupo";
  
        let nombreGrupo = document.createElement("div");
        nombreGrupo.id = "nombreGrupo";
        nombreGrupo.innerHTML = response[index]["nombreGrupo"]
        grupo.appendChild(nombreGrupo);
  
        listaGrupos.appendChild(grupo);
        
      }
    }else{
      response.forEach(e => {
        let grupo = document.createElement("div");
        grupo.className = "grupo";
  
        let nombreGrupo = document.createElement("div");
        nombreGrupo.id = "nombreGrupo";
        nombreGrupo.innerHTML = e["nombreGrupo"]
        grupo.appendChild(nombreGrupo);
  
        listaGrupos.appendChild(grupo);
      });
    }

    var grupos = document.querySelectorAll('.grupo')
    grupos.forEach(e => {
    
      e.addEventListener("click",() =>{
        let nombre = e.querySelector('#nombreGrupo')
        alert(nombre.innerHTML)
        eleccionGrupo.innerHTML = ""
        findCancion(nombre.innerHTML)
      })
  
    });

}

function findCancion(grupo){
  $.ajax({
    url:"Controller",
    data:{
      ACTION : "USUARIO.FINDCANCION",
      GRUPO : grupo
    },
    datatype : "json",
    success: function(responseText){
      console.log(responseText)
      showSongs(responseText)
    }
  })
}
function showSongs(response){

  let responseJSON = JSON.parse(response)
  let listaCanciones = document.createElement("div")
  listaCanciones.id = "listaCanciones"

  responseJSON["listaCanciones"].forEach(e => {
    
    let cancion = document.createElement("div")
    cancion.className = "cancion"
  
    let nombreCancion = document.createElement("div")
    nombreCancion.id = "nombreCancion"
    nombreCancion.innerHTML = e
    
    cancion.appendChild(nombreCancion)
    listaCanciones.appendChild(cancion)

  });

  eleccionCancion.appendChild(listaCanciones)

}
