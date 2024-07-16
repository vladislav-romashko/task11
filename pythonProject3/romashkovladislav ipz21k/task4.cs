using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Task_4_pz
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e) // Run button
        {
            double x0, y0, x1, y1;
            bool isX0Valid = double.TryParse(textBox1.Text, out x0);
            bool isY0Valid = double.TryParse(textBox2.Text, out y0);
            bool isX1Valid = double.TryParse(textBox3.Text, out x1);
            bool isY1Valid = double.TryParse(textBox4.Text, out y1);

            if (!isX0Valid)
            {
                x0 = 2;
                textBox1.Text = "2";
                textBox1.ForeColor = Color.Red;
            }
            else
            {
                textBox1.ForeColor = Color.Black;
            }

            if (!isY0Valid)
            {
                y0 = 2;
                textBox2.Text = "2";
                textBox2.ForeColor = Color.Red;
            }
            else
            {
                textBox2.ForeColor = Color.Black;
            }

            if (!isX1Valid)
            {
                x1 = 2;
                textBox3.Text = "2";
                textBox3.ForeColor = Color.Red;
            }
            else
            {
                textBox3.ForeColor = Color.Black;
            }

            if (!isY1Valid)
            {
                y1 = 2;
                textBox4.Text = "2";
                textBox4.ForeColor = Color.Red;
            }
            else
            {
                textBox4.ForeColor = Color.Black;
            }

            double distanceA = Math.Sqrt(x0 * x0 + y0 * y0);
            double distanceB = Math.Sqrt(x1 * x1 + y1 * y1);

            textBox6.Text = distanceA.ToString();
            textBox5.Text = distanceB.ToString();

            if (distanceA < distanceB)
            {
                textBox7.Text = "Точка A ближче до початку координат.";
            }
            else if (distanceA > distanceB)
            {
                textBox7.Text = "Точка B ближче до початку координат.";
            }
            else
            {
                textBox7.Text = "Обидві точки на однаковій відстані від початку координат.";
            }
        }

        private void button2_Click(object sender, EventArgs e) // About button
        {
            MessageBox.Show("Завдання: Визначити, яка з точок А або В найменш віддалена від початку координат О (0, 0).\nСтудент: [Ромашко Владислав]", "About");
        }

        private void button3_Click(object sender, EventArgs e) // Exit button
        {
            this.Close();
        }
    }
}
