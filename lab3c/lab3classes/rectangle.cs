using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class rectangle : figure
{
	private string name = "Rectangle";
	private double width;
	private double height;
	private Color color;
	public rectangle(double w, double h, Color c)
	{
		width = w; 
		height = h; 
		color = c;
	}
	public override double calc_square()
	{
		return width * height;
	}
	public string get_name()
	{
		return name;
	}
	public override string ToString()
	{
		return $"Name: {get_name()}; width: {width}; height: {height}; RGB: {color.Red},{color.Green},{color.Blue}; square: {calc_square()}";
	}
}
