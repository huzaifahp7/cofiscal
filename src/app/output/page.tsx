"use client";
import LoanApplicationForm from "@/components/userinput";
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

  useEffect(() => {
    fetch("http://127.0.0.1:5000/model", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => setApiData(data))
    .catch((error) => console.error(error));
  }, [])

  return (
    <main>
      <div className="text-3xl text-center">{apiData}</div>
    </main>
  );
}
