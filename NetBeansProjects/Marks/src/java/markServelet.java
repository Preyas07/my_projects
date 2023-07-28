import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class markServelet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter pw = res.getWriter();
        int eng = Integer.parseInt(req.getParameter("english"));

        if(eng>=40) {
            pw.print("Pass");
        } 
        else {
            pw.print("Fail");
        }
        pw.close();
    }
}
