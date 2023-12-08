/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import model.MotorSQL;
import model.bean.Grupo;
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
    
    public ArrayList<Grupo> findAll(String grupo){
        
        ArrayList<Grupo>lista = new ArrayList<>();
        String sql = SQL_FIND_ALL;
        
        try{
            motorsql.connect();
            sql+= "AND UPPER(nombreGrupo) LIKE '%" + grupo.toUpperCase() + "%' ";
             
            System.out.println(sql);
            ResultSet rs = motorsql.executeQuery(sql);
            while(rs.next()){
                Grupo grupos = new Grupo();
                grupos.setNombreGrupo(rs.getString(2));
                grupos.setId_grupo(rs.getString(1));
                lista.add(grupos);
            }
            for (Grupo e : lista) {
                sql = "SELECT * FROM CANCION WHERE id_grupo = ";
                sql += "'" + e.getId_grupo() + "' ";
                rs = motorsql.executeQuery(sql);
                while(rs.next()){
                    e.addSong(rs.getString(3));
                }
            }
            
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }finally{
            motorsql.disconnect();
        }
        return lista;
        
    }

    public Grupo findCancion(String grupo){

        Grupo grupos = new Grupo();
        String sql = SQL_FIND_ALL;
        
        try{
            motorsql.connect();
            sql+= "AND UPPER(nombreGrupo) LIKE '" + grupo.toUpperCase() + "' ";
             
            System.out.println(sql);
            ResultSet rs = motorsql.executeQuery(sql);
            
            while(rs.next()){

                grupos.setNombreGrupo(rs.getString(2));
                grupos.setId_grupo(rs.getString(1));
            }
                
            
            
            sql = "SELECT * FROM CANCION WHERE id_grupo = ";
            sql += "'" + grupos.getId_grupo() + "' ";
            rs = motorsql.executeQuery(sql);
            while(rs.next()){
                grupos.addSong(rs.getString(3));
            }
            
            
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }finally{
            motorsql.disconnect();
        }
        return grupos;
        
    }

}
