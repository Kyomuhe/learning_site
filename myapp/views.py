from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def index (request):
    return render(request, 'index.html')
def main (request):
    return render(request, 'main.html')
def datatypes (request):
    return render(request, 'datatypes.html')
def datastorage (request):
    code4 = """
     class Student{
       String regNo;
       int age;
       String name;
       public static void main(String[] args) {
          int marks=98;
          }
    }
"""
    return render(request, 'datastorage.html', {'code4': code4})
def classes(request):
    code5 = """
    class Student{
    
    }
"""
    code6 = """
    class Student{
         public static void main(String[] args) {
         }
    }
"""
    code7 = """
     class Student{
       static int x = 1;
       static String name = "Student"
        public static void main(String[] args) {
           System.out.println(name);
           System.out.println(X);
     }
"""
    return render(request, 'classes.html', {'code5': code5, 'code6': code6, 'code7': code7})
def objects(request):
    code8 = """
    class Student{
       int age;
       String name;
        public static void main(String[] args) {
            Student student1 = new Student();
            Student student2 = new Student();
            student1.name="precious";
            student2.name="jeremy";
            student1.age=20;
            student2.age=29;
            System.out.println("student1: " + student1.name+" is" + student1.age+ "years old");
            System.out.println("student2: " + student2.name+" is" + student2.age+ "years old");

       }
    }
"""
    return render(request, 'objects.html', {'code8':code8})
def classobj(request):
    java_code = """
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }
    """
    return render(request, 'classobj.html', {'java_code': java_code})
def visibility(request):
    code9 = """
    public class Person{
        public String name;
        protected int age;
        private String contact;
        double weight;
     }
    public class Student extends Person{
       public static void main(String[] args){
           Student obj = new Student();
           System.out.println(obj.name);//name is accessible 
           System.out.println(obj.age);//age is accessible 
           System.out.println(obj.contact);//contact is not accessible and so this line will cause an error
           System.out.println(obj.weight);//weight is accessible

       }
    }
"""
    return render(request, 'visibility.html', {'code9':code9})
def arrays(request):
    code11 = """
     int[] numbers= {1,2,3,4,5,6};
"""
    code12 = """
     System.out.println(numbers[0]);
"""
    code13 = """
    numbers[1] = 20;
"""
    code14 = """
    System.out.println(numbers.length)// ouput:6
    """
    code15 = """
    for(int numbers:num){
       System.out.println(num);}
"""
    code16 = """
    int[][] numbers ={{1,2,3},{4,5,6}};
    """
    code17 = """
    System.out.println(numbers[1][1]);//output:5
"""
    code18 = """
    numbers[0][0]=0;
    System.out.println([0][0]);
"""
    code19 = """
    public class Arrays {
      public static void main(String[] args){
        int[][] numbers = {{1,2,3},{4,5,6}};
        for(int i=0;i< numbers.length;++i){
            for(int j=0; j< numbers[i].length; ++j){
                System.out.println(numbers[i][j]);
            }
        }
    }
}
"""
    return render(request, 'arrays.html', {'code11':code11, 'code12':code12, 'code13':code13, 'code14':code14,
                                            'code15':code15, 'code16':code16, 'code17':code17, 'code18':code18, 'code19':code19})
def constructors(request):
    code10 = """
    public class Student {
       public String name;
       public int age;

       public Student(String name, int age) {
	      this.name = name;
	      this.age=age;
    }
        public static void main(String[] args) {
	        Student obj = new Student("precious",20);
	        System.out.println("my name is "+" "+obj.name+" "+"and iam "+obj.age+" years" );
    }

    }
"""
    return render(request, 'constructors.html', {'code10':code10})
def program(request):
    code20 = """
            public class Loop {
        public static void main(String[] args) {
        	int x =1;
        	while(x<=10) {
        		System.out.println(x);
        		x++;
        	}
             }
               }
               
               
    
"""
    code21 = """
   public class Loop2 {
public static void main(String[] args) {
	int row = 5, col; //double declaration
	while(row>0) {
		col =3;
		while(col>0) {
			System.out.print("*"); col--;
     }
		System.out.println(); row--;
	   }
         }
           }

    """
    code22 = """
     do{
     //statements to be executed;
     }while(condition);
"""
    code23 = """
            public class DoWhile {
        public static void main(String[] args) {
        	int x=1;
        	do {
        		System.out.println(x);x++;
        	}while(x<=10);
                }
               }
               
               //example 2:
               
        public class Constructor {
	
        public static void main(String[] args) {
	        int x =1;
	        do {
		       if(x%2==0)
			       System.out.println(x+" is even");
		       else
			       System.out.println(x+" is odd");
		    x++;
	}while(x<=10);
}
       }

"""
    return render(request, 'program.html', {'code20':code20, 'code21':code21, 'code22':code22, 'code23':code23})
def ife(request):
    code27 = """
        public class Precious {        	
          public static void main(String[] args) {
               int age=20;
        	if(age>=18) {
        		System.out.println(age + " years old is a sufficient age to login,Welcome!!!");
        	}else {
        		System.out.println(age +"years is not old enough to login sorry ");
        	}
        }
               }
               
               //example2:
               
        public class Example {
        public static void main(String[] args){
        	int age=50;
	       if (age > 0 && age < 18)  {
		       System.out.println(age + " years old is not sufficient age to login,sorry!!!");
	       }else if (age > 18 && age < 30) {
		       System.out.println(age +" years is sufficient enough to login ,Welcome ");
	         }
	       else {
		        System.out.println(age + " years is the best age to login ,feel at home ,Welcome");
	               }
                     }
                        }
"""
    return render(request, 'ife.html', {'code27':code27})

def inherritance(request):
    code28 = """
        public class People {
        	 String name = "precious";

        	public void eat() {
        		System.out.println("hey iam from the supper class");
        	}
           public static void main(String[] args) {
        	    Student stu = new Student();
        	    stu.eat();
        	    stu.type();
        	    System.out.println(stu.name);
        	
        }
               }

        class Student extends People{
        		public void type() {
        			System.out.println("hey iam a sub class or you can call derived class");
        		}
        	}
    
        """
    return render(request, 'inherritance.html', {'code28':code28})

def input(request):
    code29 = """
    import java.util.Scanner;  // Import the Scanner class
    public class Input {
        public static void main(String[] args) {
	        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
	        System.out.println("Enter username");

	        String userName = myObj.nextLine();  // Read user input
	        int age = myObj.nextInt();
	        System.out.println("Username is: " + userName);  // Output user input
	        System.out.println("Age is : " + age);
  }
}
"""
    return render(request, 'input.html', {'code29':code29})

def polymorphism(request):
    code30 = """
    public class Polymorphism {
        public void print() {
	        System.out.println("i belong to the super class and if iam printed there was no method overriding");
  }
	    public static void main(String[] args) {
		    SubClass obj = new SubClass();
		    obj.print();
	}
}
    class SubClass{
        @override
	    public void print() {
		    System.out.println("super class method has been overridden and this is the new implementation");
	}
}
"""
    return render(request, 'polymorphism.html', {'code30':code30})
def overloading(request):
    code31 = """
            public class Overloading {
        	public int add(int x, int y) {
               	System.out.println("from int");
        		return(x+y);
        	}
     
        	public double add(double x, double y) {
                System.out.println("from double");
        		return(x+y);
        	}
        	public static void main(String[] args) {
        		Overloading obj = new Overloading();
        		System.out.println("int value " +obj.add(5,3));
        		System.out.println("double value " +obj.add(5.2,3));
        	}

        }
"""
    return render(request, 'overloading.html', {'code31':code31})
def abstraction(request):
    code32 = """
    public abstract class Animals {
        public abstract void eat();
        }
        class Goat extends Animal{
            public void eat(){
                System.out.println("i eat grass");
            }
        }
        class Lion extends Animal{
            public void eat(){
                System.out.println("i eat meat");
            }
        }
        class Main{
            public static void main(String[] args){
                Goat obj1 = new Goat();
                Lion obj2 = new Lion();
                obj1.eat();
                obj2.eat();
            }

        }
"""
    return render(request, 'abstraction.html', {'code32':code32})
def exception(request):
    code33 = """
    public class People {
   
       public static void main(String args[]) {
          int num[] = {1, 2, 3, 4};
          System.out.println(num[5]);
   }
}


"""
    return render(request, 'exception.html', {'code33':code33})

def exception2(request):
    code34 = """
    try {
   // Protected code
} catch (ExceptionName e1) {
   // Catch block
}

"""
    code35 = """
    public class ClassName {

       public static void main(String args[]) {
          int a[] = {1,2};
          try {
               System.out.println("Access element three :" + a[3]);
          } catch (ArrayIndexOutOfBoundsException e) {
               System.out.println("Exception thrown  :" + e);
          }finally {
            System.out.println("First element value: " + a[0]);
            System.out.println("The finally statement is executed");
      }
   }
}
"""
    return render(request, 'exception2.html', {'code34':code34, 'code35':code35})
def exception3(request):
    code36 = """
     public class UserNotFoundException extends Exception {
        public UserNotFoundException (String x) {
	    super(x);
    }
    }
    class Student{
	   static String  name;
	   public static String myMethod(String name)throws UserNotFoundException {
		  if(name.equals("precious")) {
			 return "you are looged in";
		  }else {
			 throw new UserNotFoundException ("you are not found");
		}
	}
	    public static void main (String[] args)throws UserNotFoundException {
		     System.out.println(myMethod("precious"));
	}
}
"""
    return render(request, 'exception3.html', {'code36':code36})
def immutability(request):
    code37 = """
     final class ImmutableStudent{
	 private final int age;
	 private final String name;
	ImmutableStudent(int age, String name){
		this.age= age;
		this.name=name;
	}
	public static void main(String[] args) {
		ImmutableStudent obj = new ImmutableStudent(19,"precious");
		System.out.println(obj.name +" "+obj.age);
	}
}
"""
    return render(request, 'immutability.html', {'code37':code37})
def interning(request):
    code38 = """
    String name ="precious kay";//is the same as
    String name = new String("precious kay");
"""
    code39 = """
public class Interning {
static String str=new String ("precious kay").intern();
static String str1=new String("precious kay").intern();
static String str2= new String ("precious kay");
static String str3 ="precious kay";
	public static void main(String[] args) {
System.out.println(str.equals(str1));//prints true
System.out.println(str==str1);//prints true
System.out.println(str==str2);//prints false
System.out.println(str==str3);//prints true
System.out.println(str3.equals(str2));//prints true


	}

}

"""
    return render(request, 'interning.html', {'code38':code38, 'code39':code39})
def chaining(request):
    code40 = """
    
public class Temp {
	Temp(){
		this(5);
		System.out.println("this is the default constructor");

	}
	Temp(int x){
		this(5,15);
		System.out.println(x);

	}
	Temp(int x, int y){
		System.out.println(x*y);
	}

	public static void main(String[] args) {
Temp myT =new Temp();
	}

}

"""
    code41 = """
    class Parent {
    public Parent() {
        System.out.println("iam from parent");
    }
}
    class Child extends Parent{
    int age;
    public Child() {
        super();
        System.out.println("iam from child");

    }
    public Child(int age) {
        super();
        this.age=age;
        System.out.println(age);
    }
    public static void main(String[] args) {
        Child c = new Child(20);
    }
}
"""
    code42 = """
    class Base {
    String name;
    Base(){
        //this("");
        System.out.println("from the base class");
    }
    Base(String name){
        this.name=name;
        System.out.println("paramaterised constructor from the base class");
    }
}
class Baby extends Base{

    Baby(){
        System.out.println("from the baby class");

    }
    Baby(String name){
        super("kay");
        System.out.println("paramaterised constructor of baby class"+" "+name);

    }
    public static void main(String[] args) {
        Baby baby= new Baby("precious");

    }

}

"""
    return render(request, 'chaining.html', {'code40':code40, 'code41':code41, 'code42':code42})
def binding(request):
    code43 = """
    public class Animal {
       void eat() {
	      System.out.println("animals eat both flesh and plants depending on the animal");
}
       public static void main(String[] args) {
         Animal animal = new Animal();
	     Animal a= new Lion();
	     Animal b= new Sheep();
         animal.eat();
	     a.eat();
	     b.eat();
}
}
    class Lion extends Animal{
	    void eat() {
		   System.out.println("it eats flesh");
	}
}
    class Sheep extends Animal{
	    void eat() {
		    System.out.println("it eats plants");
	}
}

"""
    return render(request, 'binding.html', {'code43':code43})
def clone(request):
    code44 = """
    class Student implements Cloneable {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();  // Shallow copy
    }

    @Override
    public String toString() {
        return "Student [name=" + name + ", age=" + age + "]";
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            Student originalStudent = new Student("Alice", 20);
            Student clonedStudent = (Student) originalStudent.clone();

            System.out.println("Original Student: " + originalStudent);
            System.out.println("Cloned Student: " + clonedStudent);

            System.out.println("Are they the same object? " + (originalStudent == clonedStudent));
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
    }
}

"""
    return render(request, 'clone.html', {'code44':code44})
def generic(request):
    code45 = """
public class GenericClass<T> {
public T data;
public  GenericClass(T data) {
	this.data=data;
}
public T getData() {
	return this.data;
}
	public static void main(String[] args) {
		 GenericClass<Integer> n = new  GenericClass<Integer>(4);
		 GenericClass<String> g = new  GenericClass<String>("hry");
		System.out.println( n.getData());
		System.out.println( g.getData());


"""
    code46 = """
public class Oop {

public static void main(String[] args) {
Integer[] intArray = {1,2,3,4,5,6,7,8,9,10};
Double[] doubleArray = {1.0,2.0,3.0,4.0};
String[] stringArray = {"precious","kay","kyomuhendo"};
displayArray(intArray);
displayArray(doubleArray);
displayArray(stringArray);
	}
public static <T> void displayArray(T[] array) {
	for(T x :array) {
		System.out.print(x+" ");
	}
	System.out.println();
}
}


"""
    code47 = """
public class Try {

public static void main(String[] args) {
Try myTry = new Try();
myTry.<Integer>myMethod(3);
myTry.<String>myMethod("precious kay");
	}
public <T> void myMethod(T data) {
	System.out.println(data);
}
}


"""
    return render(request, 'generic.html', {'code45':code45, 'code46':code46, 'code47':code47})
def casting(request):
    code48 = """
    class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();  // Upcasting
        myDog.makeSound();  // Output: "Dog barks"
    }
}

"""
    code49 = """
    Animals a = new Cat();
    Cat c = (Cat) a;

"""
    return render(request, 'casting.html', {'code48':code48, 'code49':code49})
def inner(request):
    code50 = """
public class OuterClass1 {
  private  int x=2;
public  void myMethod() {
	System.out.println("hhf");
}
  public class InnerClass {
    public void doSomething() {
    	System.out.println(x);
    	myMethod();
    }
  }  
  public static void main(String[] args) {
	  OuterClass1 m = new OuterClass1();
	  OuterClass1.InnerClass myObj = m.new InnerClass();
	  myObj.doSomething();
	  m.myMethod();//can access outer class methods
  }
}


"""
    code51 = """
public class OuterClass {
    private int x = 10;
    static int y = 20;

    static class StaticInnerClass {
        public void display() {
            // Since the inner class is static, it cannot access non-static members of the outer class
            // System.out.println("x = " + x); // This would cause a compile-time error
            System.out.println("y = " + y);
        }
    }
}
 class Main {
    public static void main(String[] args) {
        OuterClass.StaticInnerClass inner = new OuterClass.StaticInnerClass();
        inner.display(); // Output: y = 20
    }


"""
    code52 = """
LocalClassExample{
      private String name = "Jesse";
      
      public void method ( ) {
            int j = 20;
            final int k = 30;
		
            class Local {
                  public void test ( ) {
                       System.out.println(j); //it will not bring an error since it is effectively final
                       System.out.println(k); //OK k is final
				
                       //Like an inner class, instance variables of
                      //the enclosing object can be accessed.
                      System.out.println ( name ) ;
                }
          }
          Local loc = new Local ( ) ;
          loc.test ( ) ;
    }
	
      public static void main ( String [ ] args ) {
            LocalClassExample obj = new LocalClassExample ( );
                  obj.method ( ) ;
            }
}


"""
    code53 = """
public class Precious {
	public void myMethod() {
		System.out.println("hey ,iam not from the anonymous class");
	}
public static void main(String[] args) {
	Kay myKay = new Kay() {//start of anonymous class
		private int number;
		public void setNumber(int number) {
			this.number=number;
		}
		public int getNumber() {
			return number;
		}

	};//end of anonymous class
	myKay.setNumber(23);
	System.out.println(myKay.getNumber());
	System.out.println("program finished");
	Precious myPrecious = new Precious();
	myPrecious.myMethod();
	//myKay.myMethod();
}
}

"""
    return render(request, 'inner.html', {'code50':code50, 'code51':code51, 'code52':code52, 'code53':code53})
def serialize(request):
    code54 = """
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;
public class Student implements Serializable {
String name;
String religion;
String rollNo;

	public Student(String name, String religion, String rollNo) {
	this.name = name;
	this.religion = religion;
	this.rollNo = rollNo;
}
	public Student() {
		
	}
public void objectSerialization(Student stu)throws IOException {
	FileOutputStream fos = new FileOutputStream("student.ser");
	ObjectOutputStream oos= new ObjectOutputStream(fos);
	oos.writeObject(stu);
	oos.close();
	fos.close();
	System.out.println("student.ser");
}
	public static void main(String[] args) throws IOException{
Student stu = new Student("precious kay","protestant","3333");
stu.objectSerialization(stu);
	}

}

"""
    return render(request, 'serialize.html', {'code54':code54})
def deserialize(request):
    code55 = """
import java.io.*;
public class Studentinfo implements Serializable
{
    String name;
    int rid;
    String contact;
    Studentinfo(String n, int r, String c)
    {
    this.name = n;
    this.rid = r;
    this.contact = c;
    }
}

 class Test
{
    public static void main(String[] args)
    {
        try
        {
            Studentinfo si = new Studentinfo("precious", 123, "0789123456");
            FileOutputStream fos = new FileOutputStream("student2.ser");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(si);
            oos.close();
            fos.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        } }}


"""
    return render(request, 'deserialize.html', {'code55':code55})
def forl(request):
    code24 = """
     for(st1; st2; st3){ //code to be executed}
"""
    code25 = """
            public class Loop {
        public static void main(String[] args) {
        	int i;
        	for(i=0; i<=10;i++)
        		System.out.println(i);
             }
               }
               
               

"""
    code26 = """
        public class Constructor {
        public static void main(String[] args) {
	        for(int i =0;i<10;i++) {
		        for(int j=0;j<i;j++) {
			        System.out.print("*");
		}
		        System.out.println();
	      }
            }
              }

    
"""
    return render(request, 'forl.html', {'code24':code24, 'code25':code25, 'code26':code26})
def interfaces(request):
    java_code = """
    public interface interfaceName{
       // properties
       //methods
    }
    """
    kay = """
    public interface X{
       public abstract void m1();
    }
    public interface Y{
       public abstract void m2();
    }
    public interface Z extends X,Y{
    
    }

    """
    mey = """
      public interface X{
        public abstract void m1();
        public static final k=10;
      }
      //is equivalent to
      public interface X{
         void m1();
         int k = 10;
      }
    """
    hey = """
     public interface X{
        default void m1(){
        System.out.println("hello iam default");
        }
        public static void m2(){
        System.out.println("hello iam static");
        }
     }
    """
    code3 = """
    public interface X {
    static void m3() {
        System.out.println("I am from X and I have been successfully implemented");
    }
}

interface Y {
    default void m() {
        System.out.println("I am from Y and I have been successfully implemented");
    }
}

public class Z implements X, Y {
    public static void main(String[] args) {
        Z obj = new Z();
        X.m3();  // You can call static methods using the interface name
        obj.m(); // You can call default methods on an object implementing the interface
    }
}

    """
    return render(request, 'interfaces.html', {'java_code': java_code, 'kay': kay, 'mey': mey, 'hey':hey, 'code3': code3})

    #return (render(request, 'interfaces.html', {'java_code': java_code}))

