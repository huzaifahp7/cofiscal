import "./globals.css";
import type { Metadata } from "next";
import { Inter, Montserrat } from "next/font/google";
import { Providers } from "./providers";

const inter = Inter({ subsets: ["latin"] });

const montserrat = Montserrat({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "CoFiscal",
  description: "Loan Management System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="light">
      <body className={`${inter.className} ${montserrat.className}`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
