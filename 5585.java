import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner stdin = new Scanner(System.in);

        int coin = 0;
        int money = stdin.nextInt();
        int change = 1000 - money;

        while(true){
            if(change >= 500){
                change -= 500;
                coin++;
            }
            else if(change >= 100){
                change -= 100;
                coin++;
            }
            else if(change >= 50){
                change -= 50;
                coin++;
            }
            else if(change >= 10){
                change -= 10;
                coin++;
            }
            else if(change >= 5){
                change -= 5;
                coin++;
            }
            else{
                change -= 1;
                coin++;
            }

            if(change == 0){
                break;
            }
        }
        System.out.print(coin);
    }
}
