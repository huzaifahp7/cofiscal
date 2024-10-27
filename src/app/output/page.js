"use client";
import Header from "@/components/header";
import UserOutput from "@/components/useroutput";
import Image from "next/image";
import { useSearchParams } from "next/navigation";
import { useDebugValue, useEffect, useState } from "react";

export default function Output() {
  const searchParams = useSearchParams();

  const [formData, setFormData] = useState({
    age: searchParams.get("age"),
    income: searchParams.get("income"),
    loanAmount: searchParams.get("loanAmount"),
    creditScore: searchParams.get("creditScore"),
    monthsEmployed: searchParams.get("monthsEmployed"),
    creditLines: searchParams.get("creditLines"),
    interestRate: searchParams.get("interestRate"),
    loanTerm: searchParams.get("loanTerm"),
    debtToIncomeRatio: searchParams.get("debtToIncomeRatio"),
    education: searchParams.get("education"),
    employmentType: searchParams.get("employmentType"),
    maritalStatus: searchParams.get("maritalStatus"),
    mortgage: searchParams.get("mortgage"),
    dependents: searchParams.get("dependents"),
    loanPurpose: searchParams.get("loanPurpose"),
    coSigner: searchParams.get("coSigner"),
  });

  const [apiData, setApiData] = useState();
  const [result, setResult] = useState();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("http://127.0.0.1:5000/model", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const data = await response.json();
        setApiData(data);

        // Now you can update formData with apiData.prediction
        const updatedFormData = {
          ...formData,
          prediction: data.prediction,
        };

        // Set the updated form data
        setFormData(updatedFormData);

        // Fetch the next data after 5 seconds
        setTimeout(async function () {
          const response = await fetch("http://127.0.0.1:5000/gpt", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(updatedFormData), // Use the updated data
          });

          if (!response.ok) {
            throw new Error("Network response was not ok");
          }

          const resultData = await response.json();
          setResult(resultData);
          setLoading(true);
        }, 5000);
      } catch (error) {
        console.error(error);
      }
    }

    fetchData();
  }, [formData]);

  return (
    <div>
      {loading ? (
        <div>
          <Header />
          <UserOutput data={apiData} formData={formData} result={result} />
        </div>
      ) : (
        <div className="h-[100vh] w-full items-center justify-center flex flex-col">
          <Image
            src={"/images/loading.gif"}
            alt="Loading gif"
            width={500}
            height={500}
          ></Image>
          <span className="text-black text-[48px] font-medium mt-2">
            Loading your insights
          </span>
          <span className="text-black text-[28px] font-normal mt-4">
            Crunching the numbers, calculating the values...
          </span>
        </div>
      )}
    </div>
  );
}
