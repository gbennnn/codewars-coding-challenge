public class Main {
    public static void main(String[] args) {
        int yearsAgo;
        try {
            yearsAgo = TwiceAsOld.TwiceAsOld(30, 5);
            System.out.println("Years ago : " + yearsAgo);
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
