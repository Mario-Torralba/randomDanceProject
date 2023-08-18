const listaGrupos = document.getElementById("listaGrupos");

document.body.addEventListener("load", initComponents());

function initComponents() {
  const inputGrupo = document.getElementById("inputGrupo");

  inputGrupo.addEventListener("submit", () => {
    let inputGrupo = document.getElementById("inputGrupo");

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
      grupo.id = "grupo";

      let nombreGrupo = document.createElement("div");
      nombreGrupo.id = "nombreGrupo";
      nombreGrupo.innerHTML = response[index]["nombreGrupo"]
      grupo.appendChild(nombreGrupo);

      listaGrupos.appendChild(grupo);
    }
  } catch {
    console.log("Error en el try")
  }
}
