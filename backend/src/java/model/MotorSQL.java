/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;




import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author yo
 */
public class MotorSQL {
    
    private Connection conn;
    private Statement st;
    private ResultSet rs;
    
    private static final String URL = "jdbc:postgresql://random-db:5432/postgres";
    private static final String CONTROLADOR = "org.postgresql.Driver";
    private static final String USER = "postgres";
    private static final String PASSWORD = "1234";
    
    public void connect(){
        System.out.println(DriverManager.getDrivers().toString());
        try{
            Class.forName(CONTROLADOR);
            conn = DriverManager.getConnection(URL, USER, PASSWORD);
            st = conn.createStatement();
        }catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }
    
    public int execute(String sql) {
        int resp = 0;
        try {
            resp = st.executeUpdate(sql);
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
        return resp;
    }

    public ResultSet executeQuery(String sql) {
        try {
            rs = st.executeQuery(sql);
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
        return rs;
    }
    
    public void disconnect(){
        try{
            if(rs != null){
                rs.close();
            }
            if(st != null){
                st.close();
            }
            if(conn != null){
                conn.close();
            }
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
    }
    
}
