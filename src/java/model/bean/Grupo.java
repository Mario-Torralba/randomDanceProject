/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.bean;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.ArrayList;

/**
 *
 * @author yo
 */
public class Grupo {
    
    String nombreGrupo;
    String id_grupo;
    ArrayList<String>listaCanciones;
    
    public Grupo(){
        listaCanciones = new ArrayList<>();
    }
    
    public static String toArrayJson(ArrayList<Grupo>lista){
        GsonBuilder builder = new GsonBuilder();
        builder.setPrettyPrinting();

        Gson gson = builder.create();
        String resp = gson.toJson(lista);

        return resp;
    }

    public static String toArrayJsonIndividual(Grupo lista){
        GsonBuilder builder = new GsonBuilder();
        builder.setPrettyPrinting();

        Gson gson = builder.create();
        String resp = gson.toJson(lista);

        return resp;
    }

    public void addSong(String cancion){
        listaCanciones.add(cancion);
    }
    public String getNombreGrupo() {
        return nombreGrupo;
    }
    public void setNombreGrupo(String nombreGrupo) {
        this.nombreGrupo = nombreGrupo;
    }
    public ArrayList<String> getListaCanciones() {
        return listaCanciones;
    }
    public void setListaCanciones(ArrayList<String> listaCanciones) {
        this.listaCanciones = listaCanciones;
    }

    public String getId_grupo() {
        return id_grupo;
    }

    public void setId_grupo(String id_grupo) {
        this.id_grupo = id_grupo;
    }
}
