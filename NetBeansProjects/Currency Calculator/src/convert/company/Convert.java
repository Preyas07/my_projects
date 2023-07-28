package convert.company;
import java.io.*;
import java.net.*;
import java.util.*;
class Recv
{
private String lhs;
private String rhs;
private String error;
private String icc;
public Recv()
{
}
public String getLhs()
{
return lhs;
}
public String getRhs()
{
return rhs;
}
}
public class Convert extends HttpServlet {
 protected void processRequest(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String query = "";
        String amount = "";
        String curTo = "";
        String curFrom = "";
        String submit = "";
        String res = "";
        HttpSession session;
        resp.setContentType("text/html;charset=UTF-8");
        PrintWriter out = resp.getWriter();
        //Read request parameters//
        amount = req.getParameter("amount");
        curTo = req.getParameter("to");
        curFrom = req.getParameter("from");
        //Open a connection to google and read the result//

        try {
            query = "http://www.google.com/ig/calculator?hl=en&q=" 
                    + amount + curFrom + "=?" + curTo;
 URL url = new URL(query);
            InputStreamReader stream = new InputStreamReader(url.openStream());
            BufferedReader in = new BufferedReader(stream);
            String str = "";
            String temp = "";
            while ((temp = in.readLine()) != null) {
                str = str + temp;
            }

            //Parse the result which is in json format//
            Gson gson = new Gson();
            Recv st=gson.fromJson(str, Recv.class);
            String rhs = st.getRhs();
            rhs = rhs.replaceAll("�", "");
            //we do the check in order to print the additional word(millions,billions etc)//
            StringTokenizer strto = new StringTokenizer(rhs);
String nextToken;

            out.write(strto.nextToken());
            nextToken = strto.nextToken();

            if( nextToken.equals("million") || nextToken.equals("billion") || nextToken.equals("trillion"))
            {
                out.println(" "+nextToken);
            } 
        } catch (NumberFormatException e) {
            out.println("The given amount is not a valid number");
        }
    }
}


