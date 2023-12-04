using System;
public class square : figure
{
	private static string name = "circle";
	private int length;
	private Color color;

	public square(int r, Color c)
	{
		this.length = r;
		this.color = c;
	}

	public override double calc_square()
	{
		return length*length;
	}

	public static string get_name()
	{
		return name;
	}

	public override string ToString()
	{
		return $"Name: {get_name()}; length: {length}; RGB: {color.Red},{color.Green},{color.Blue}; square: {calc_square()}";
	}
}
