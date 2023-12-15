public class diffshapes 
{
    public static void main(String[] args) 
    {
        double height, width, base, radius, perimeter, area;
        System.out.println("Geometric Shapes");
    
            // Triangle
            System.out.println("\nTriangle");
            height = 10;
            base = 15;
            perimeter = 2 * (height + base / 2);
            area = 0.5 * base * height;
            System.out.println("Perimeter = " + perimeter);
            System.out.println("Area = " + area);
    
            // Rectangle
            System.out.println("\nRectangle");
            height = 10;
            width = 15;
            perimeter = 2 * (height + width);
            area = height * width;
            System.out.println("Perimeter = " + perimeter);
            System.out.println("Area = " + area);
    
            // Circle
            System.out.println("\nCircle");
            radius = 10;
            perimeter = 2 * Math.PI * radius;
            area = Math.PI * Math.pow(radius, 2);
            System.out.println("Perimeter = " + perimeter);
            System.out.println("Area = " + area);
        }
    }
    
