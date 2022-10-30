// Methods don't exist for primitive variable
// Only on non prmitive variables, like String
// They can be distinguished becausde prmitive are all lower case, while non prmitive start with 
// uppercase


// Primitive data types:
// - Byte, short, long and int for whole numbers
// - float and double for fractional numbers
// - char for characters
// - bool for T/F
//##############################################################################
// Byte goes from -128 to 127
// Short goes from -32,768 to 32767
// Int goes from  -2,147,483,648 to 2,147,483,647
// Long goes from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
//##############################################################################
// Double holds 15 decimal digits
// Float holds from 6 to 7. ALWAYS suffix float with an "f", else compiler will assume double. Eg 22.4f

// Classes don't need to be imported. As long as they are in the same folder 

public class myOwnClass {

    // Static methods  can be used without creating an object
    // Private means it is a method you can only use while inside the class. 
    // Public means it can be accesed anywhere
    private static String printName(String name, int number) {
        

        // In conditionals for comparing strings use str.equals()
        // In the case of numbers use var == 5

        if (name.equals("John")) {

            System.out.println("This name is cool");

        }
        else if (name.equals("Gabriel")) {

            System.out.println("This is the best name");

        }
        else {

            System.out.println("I don't know this name");

        }
        
        return "My  name is" + name ;
    }

    public static void main(String[] args){


        // Declaring primtive variables 
        int Var = 7;
        double ShoeSize = 12.5  ;
        char myInitial = 'J' ;

        // Declaring non primtive variables

        String myName = "Gabriel" ;

        // Non prmitive variables have methods 

        myName.length() ;
        String AnotherName = myName.concat(myName) ;

        // Operations can be performed on the different variables
        double resultMulti = Var * ShoeSize ;
        double resultSum = Var + ShoeSize ;
        double resultSubs = Var - ShoeSize ;
        double resultDiv = Var / ShoeSize ;

        // In order to print use this command
        //If you want to print multiple things on the same line there are multiple options 
        //*****************************************************
        // System.out.print("My Shoe Size is ");
        // System.out.println(ShoeSize);
        // OR
        // System.out.println("My Shoe Size is " + ShoeSize);
        //***************************************************** */

        System.out.print("My Shoe Size is ");
        System.out.println(ShoeSize);
        System.out.print("My Name is ");
        System.out.print(myName);
        System.out.print(" and it's ");
        System.out.print(myName.length());
        System.out.println(" characters long.");

        //Calling a method is easy

        String name = printName(myName, Var) ;


        // for loops can be used to iterate over, a certain amount of times
        for (int i = 0; i < 10; i++){

            System.out.println("Hello World " + i);

        }

        // You can call other classes methods as long as they are public
        Cat.dingDong();

        //You can also create objects by defining them,  and their attributes too
        Cat myCat = new Cat() ;
        myCat.name = "Lily" ;
        myCat.age = 5 ;
        Cat anotherCat =new Cat() ;
        anotherCat.name = "Nessie" ;
        anotherCat.age = 3 ;
        

    }

}
