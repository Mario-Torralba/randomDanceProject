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
    ArrayList<Cancion>listaCanciones;
    
    public Grupo(String nombre){
        this.nombreGrupo = nombre;
        listaCanciones = new ArrayList<>();
    }
    
    public static String toArrayJson(ArrayList<Grupo>lista){
        GsonBuilder builder = new GsonBuilder();
        builder.setPrettyPrinting();

        Gson gson = builder.create();
        String resp = gson.toJson(lista);

        return resp;
    }
}
