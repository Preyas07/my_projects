/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;


/**
 *
 * @author preya
 */
public class cookie_pro extends HttpServlet {

   
      @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter pw = res.getWriter();
        String d = req.getParameter("data");
        Cookie co = new Cookie("mycookie","india");
        res.addCookie(co);
        pw.println("<b> cookie has been sent to "+d);
        pw.print("<a href ='cookie_val'>view details</a>");
        pw.close();
    }

    

}
