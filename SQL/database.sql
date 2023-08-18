DROP TABLE GRUPO;
DROP TABLE CANCION;

CREATE TABLE GRUPO(
    id_grupo VARCHAR(6) NOT NULL,
    nombreGrupo VARCHAR(200) NOT NULL,
    imagenGrupo VARCHAR(200) NOT NULL,
    PRIMARY KEY (id_grupo)
);

CREATE TABLE CANCION(
    id_cancion INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 0, INCREMENT BY 1),
    id_grupo VARCHAR(6) NOT NULL,
    nombreCancion VARCHAR(200) NOT NULL,
    PRIMARY KEY (id_cancion)
);

 -- /////////////////////////////////////////////////


