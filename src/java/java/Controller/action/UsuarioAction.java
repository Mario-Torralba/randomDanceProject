/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java.Controller.action;

import java.model.beans.Grupo;

import java.util.ArrayList;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.model.dao.UsuarioDAO;

/**
 *
 * @author yo
 */
public class UsuarioAction {
    
    
    public String execute(HttpServletRequest request, HttpServletResponse response) {
        String pagDestino = "";
        String action = request.getParameter("ACTION");

        String[] arrayAction = action.split("\\.");
        switch (arrayAction[1]) {
            case "FINDALL":
                pagDestino = findall(request, response);
                break;
        }
        return pagDestino;
    }
    public String findall(HttpServletRequest request, HttpServletResponse response){
        UsuarioDAO usuariodao = new UsuarioDAO();
        ArrayList<Grupo> lista = usuariodao.findAll(request.getParameter("GRUPO"), request.getParameter("CANCION"));
        //return Grupo.toArrayJson(lista);
        return "hola";
    }
}
