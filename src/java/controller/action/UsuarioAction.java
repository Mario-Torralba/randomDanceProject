/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller.action;

import java.io.IOException;
import java.io.PrintWriter;
import model.bean.Grupo;

import java.util.ArrayList;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import model.dao.UsuarioDAO;

/**
 *
 * @author yo
 */
public class UsuarioAction {
    
    
    public String execute(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String pagDestino = "";
        String action = request.getParameter("ACTION");

        String[] arrayAction = action.split("\\.");
        switch (arrayAction[1]) {
            case "FINDALL":
                pagDestino = findall(request, response);
                break;
            case "FINDCANCION":
                pagDestino = findCancion(request, response);
                break;
        }
        return pagDestino;
    }
    public String findall(HttpServletRequest request, HttpServletResponse response) throws IOException{
        String ip = request.getRemoteAddr();
        System.out.println(ip);

        UsuarioDAO usuariodao = new UsuarioDAO();
        ArrayList<Grupo> lista = usuariodao.findAll(request.getParameter("GRUPO"));
        return Grupo.toArrayJson(lista);
    }
    public String findCancion(HttpServletRequest request, HttpServletResponse response){
        UsuarioDAO usuariodao = new UsuarioDAO();
        Grupo lista = usuariodao.findCancion(request.getParameter("GRUPO"));
        return Grupo.toArrayJsonIndividual(lista);
    }

}
