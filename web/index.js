const listaGrupos = document.getElementById("listaGrupos");
var grupos = document.querySelectorAll('.grupo')

document.body.addEventListener("load", initComponents());

function initComponents() {


  let inputGrupo = document.getElementById("inputGrupo");

  

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

  try {
    for (let index = 0; index < 10; index++) {
      let grupo = document.createElement("div");
      grupo.className = "grupo";

      let nombreGrupo = document.createElement("div");
      nombreGrupo.id = "nombreGrupo";
      nombreGrupo.innerHTML = response[index]["nombreGrupo"]
      grupo.appendChild(nombreGrupo);

      listaGrupos.appendChild(grupo);
      
    }
    var grupos = document.querySelectorAll('.grupo')
    grupos.forEach(e => {
    
      e.addEventListener("click",() =>{
        alert('a')
      })
  
    });
  } catch {
    console.log("Error en el try")
  }
}
