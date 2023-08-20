package controller.action;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class Pruebaip {
    public static void main(String[] args) throws UnknownHostException {
        InetAddress address = InetAddress.getLocalHost();
        String host = address.getHostName();
        byte[] ip = address.getAddress();
        String ipAddress = "";
	   
        
        System.out.println(ip);
    }
}
