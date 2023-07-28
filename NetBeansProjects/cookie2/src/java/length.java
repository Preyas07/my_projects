/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.*;

import javax.servlet.*;
import javax.servlet.http.*;
public class length extends HttpServlet {
@Override
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter pw = res.getWriter();
        String username= req.getParameter("un");
        pw.println("length of string "+username.length());
    }

  
}

