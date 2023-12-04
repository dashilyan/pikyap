using System;
public class circle : figure
{
	private static string name = "circle";
	private int radius;
	private Color color;

	public circle(int r, Color c)
	{
		this.radius = r;
		this.color = c;
	}

	public override double calc_square()
	{
		return Math.PI * Math.Pow(radius, 2);
	}

	public static string get_name()
	{
		return name;
	}

	public override string ToString()
	{
		return $"Name: {get_name()}; radius: {radius}; RGB: {color.Red},{color.Green},{color.Blue}; square: {calc_square()}";
	}
}
