/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import model.MotorSQL;
import java.model.beans.Grupo;
import java.sql.ResultSet;
import java.util.ArrayList;

/**
 *
 * @author yo
 */
public class UsuarioDAO {
    
    private final String SQL_FIND_ALL = "SELECT * FROM GRUPO WHERE 1=1 ";
    
    private MotorSQL motorsql;
    
    public UsuarioDAO(){
        this.motorsql = new MotorSQL();
    }
    
    public ArrayList<Grupo> findAll(String grupo, String cancion){
        
        ArrayList<Grupo>lista = new ArrayList<>();
        String sql = SQL_FIND_ALL;
        
        try{
            motorsql.connect();
            System.out.println(sql);
            ResultSet rs = motorsql.executeQuery(sql);
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }finally{
            motorsql.disconnect();
        }
        return lista;
        
    }
}
