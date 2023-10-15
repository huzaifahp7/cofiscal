'use client'
import Image from "next/image";
import Link from "next/link";
import { motion } from "framer-motion";

const HomePage = () => {
  return (
    <div className="w-full items-center flex justify-between h-[100vh] bg-gradient-to-br from-cyan-400 via-violet-700 to-violet-700  p-40">
      <div className="flex flex-col justify-start h-30%">
        <div className="text-white text-[64px] font-bold font-montserrat">
          CoFiscal
        </div>
        <div className="text-white text-4xl font-semibold font-montserrat">
          Where Loans meet Certainty
        </div>
        <Link
          href={"/input"}
          className="mt-10 w-fit border-2 border-white rounded-3xl py-3 px-8"
        >
          <span className="text-white">Compare My Loan</span>
        </Link>
      </div>
      <div>
        <Image
          src={"/images/money.gif"}
          alt="Money GIF"
          width={600}
          height={600}
        ></Image>
        
      </div>
    </div>
  );
};

export default HomePage;
