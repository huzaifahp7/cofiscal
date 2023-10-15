import { CircularProgress } from "@nextui-org/react";
import Analysis from "@/components/analysis";
import ArrowBackIosIcon from "@mui/icons-material/ArrowBackIos";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function UserOutput({ data, formData, result }) {
  var percentage = (data.prediction * 100).toFixed(2);
  
  console.log(parseInt(percentage));
  const greenBar = "bg-green-500 relative h-2 rounded-lg w-[" + "50" + "%]";
  console.log(greenBar);

  const [circleColor, setCircleColor] = useState("danger")

  const divClassName = "flex w-20 h-16 py-2 px-10 items-center justify-center font-semibold"

  useEffect(() => {
    if(percentage >= 0 && percentage <= 30) {
      setCircleColor("success")
    } else if (percentage >= 30 && percentage < 60) {
      setCircleColor("warning")
    } else {
      setCircleColor("danger")
    }
  }, [])


  return (
    <div className="w-full h-fit bg-gradient-to-br from-cyan-400 via-violet-700 to-violet-700">
      <div className="flex flex-row pt-20 ps-20">
        <Link href={"/"} className="flex">
          <button className="h-18 w-32">
            <ArrowBackIosIcon fontSize="large" className="text-white" />
          </button>
        </Link>
        <span className="w-fit text-white font-bold text-[48px] text-center align-middle">
          Results
        </span>
      </div>

      <div className="flex relative flex-col items-center px-32">
        <div className="flex items-center justify-center gap-x-32 h-fit">
          <div className="flex flex-col items-center justify-center transition ease-in-out hover:-translate-y-1 hover:scale-110">
            <CircularProgress
              classNames={{
                svg: "w-80 h-80 drop-shadow-md",
                // indicator: {circleColor(percentage)},
                track: "stroke-white/10",
                value: "text-[48px] font-semibold text-white",
              }}
              size="lg"
              color={circleColor}
              value={percentage}
              showValueLabel={true}
            />

            <span className="text-white text-[28px] font-semibold">
              Likelihood to Default
            </span>
          </div>
          <div className="w-[50%]">
            <Analysis result={result} />
          </div>
        </div>

        <div className="flex flex-col w-full">
          {result.predict.slice(5).map((item) => {
            return (
                <span key={item} className="text-white mt-4 tracking-widest text-lg">
                  {item.replaceAll('*', '')}
                </span>
            );
          })}
        </div>

        <div className="flex flex-col mt-20 items-start w-full">
          <span className="text-white  text-[48px] font-semibold">Comparison with existing cases</span>
          <span className="text-white text-[24px] font-medium mt-4">Let us compare your file against 7 similar cases to see whether they defaulted on their loans.</span>
          <span className="text-white text-base font-light mt-2">Note: We cannot account for unpredictable factors like health concerns, accidents etc. Please consider these factors before making a final decision</span>
        </div>
        

        <div className="overflow-x-auto mt-20 pb-4 w-full scrollbar scrollbar-thumb-neutral-400 scrollbar-thumb-rounded-xl">
          <div className="grid grid-cols-17 w-[140%] gap-y-5 bg-blue-400 mt-2 rounded-3xl  ">
            <div className={divClassName}>
              <span>Age</span>
            </div>
            <div className={divClassName}>
              <span>Income</span>
            </div>
            <div className={divClassName}>
              <span>Loan Amount</span>
            </div>
            <div className={divClassName}>
              <span>Credit Score</span>
            </div>
            <div className={divClassName}>
              <span>Months Employed</span>
            </div>
            <div className={divClassName}>
              <span>Credit Lines</span>
            </div>
            <div className={divClassName}>
              <span>Interest Rate(%)</span>
            </div>
            <div className={divClassName}>
              <span>Loan Term</span>
            </div>
            <div className={divClassName}>
              <span className="py-2">DTI Ratio</span>
            </div>
            <div className={divClassName}>
              <span>Education</span>
            </div>
            <div className={divClassName}>
              <span>Employment Type</span>
            </div>
            <div className={divClassName}>
              <span>Marital Status</span>
            </div>
            <div className={divClassName}>
              <span>Mortgage</span>
            </div>
            <div className={divClassName}>
              <span>Dependents</span>
            </div>
            <div className={divClassName}>
              <span>Loan Purpose</span>
            </div>
            <div className={divClassName}>
              <span>Co-signer</span>
            </div>
            <div className={divClassName}>
              <span>Defaults?</span>
            </div>
          </div>

          <div className="grid grid-cols-17 w-[140%] gap-y-5 bg-white mt-2 rounded-3xl ">
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.age}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.income}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.loanAmount}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.creditScore}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.monthsEmployed}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.creditLines}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.interestRate}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.loanTerm}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.debtToIncomeRatio}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.education}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.employmentType}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.maritalStatus}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.mortgage}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.dependents}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.loanPurpose}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{formData.coSigner}</span>
            </div>
            <div className="flex w-20 h-16 py-2 px-10 items-center justify-center">
              <span>{percentage}</span>
            </div>
          </div>
          {data.neighbour.map((neigh) => {
            return (
              <div
                key={neigh.age}
                className="grid grid-cols-17 w-[140%] gap-y-5 bg-slate-400 mt-2 rounded-3xl"
              >
                {neigh.map((cell) => {
                  return (
                    <div
                      key={cell}
                      className="flex w-20 h-16 py-2 px-10 items-center justify-center"
                    >
                      <span>{cell}</span>
                    </div>
                  );
                })}
              </div>
            );
          })}
        </div>

        <div className="mt-20"></div>
      </div>
    </div>
  );
}
