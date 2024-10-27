"use client";
import React, { useState } from "react";
import ReactSelect from "react-select";
import Router, { useRouter } from "next/navigation";
import UploadIcon from "@mui/icons-material/Upload";
import { CircularProgress } from "@nextui-org/react";

const LoanApplicationForm = () => {
  const router = useRouter();

  const [file, setFile] = useState();

  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    age: 18,
    income: 25000,
    loanAmount: 10000,
    creditScore: 400,
    monthsEmployed: 12,
    creditLines: 1,
    interestRate: 2,
    loanTerm: 18,
    debtToIncomeRatio: 0.25,
    education: 1,
    employmentType: 1,
    maritalStatus: 1,
    mortgage: 1,
    dependents: 1,
    loanPurpose: 1,
    coSigner: 1,
  });

  const [errors, setErrors] = useState({});

  const educationOptions = [
    { value: 3, label: "High School" },
    { value: 1, label: "Bachelor's" },
    { value: 2, label: "Master's" },
    { value: 4, label: "PhD" },
  ];

  const booleanOptions = [
    { value: 1, label: "Yes" },
    { value: 0, label: "No" },
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  if (file !== undefined) {
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = {};

    setErrors(newErrors);

    // If no errors, submit the form data
    if (Object.keys(newErrors).length === 0) {
      // Handle form submission, e.g., send data to the server
      console.log(formData);
      router.push("/output?" + objectToQueryString(formData));
    }
  };

  function objectToQueryString(obj) {
    const keys = Object.keys(obj);
    const keyValuePairs = keys.map((key) => {
      return encodeURIComponent(key) + "=" + encodeURIComponent(obj[key]);
    });
    return keyValuePairs.join("&");
  }

  const handleFile = async (event) => {
    setLoading(true);
    try {
      const mfile = event.target.files[0];
      if (!mfile) {
        console.log("No file selected");
        return;
      }

      console.log("File has been received");

      const fileData = new FormData();
      fileData.append("file_from_react", mfile);

      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: fileData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      const autoData = data.Read;
      const newMortgage = autoData["Has Mortgage"] === "No" ? 0 : 1;
      console.log(newMortgage);

      setFormData({
        ...formData,
        income: autoData["Income 2021"],
        creditScore: autoData["Credit Score"],
        age: autoData["Age"],
        mortgage: newMortgage,
      });

      setLoading(false);
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="w-full items-center h-fit bg-gradient-to-br from-cyan-400 via-violet-700 to-violet-700 p-40"
    >
      <div className="flex flex-col items-center justify-center">
        <span className="text-white text-[40px] font-semibold">
          Enter your details:
        </span>
        <span className=" mt-4 text-white text-[20px] font-medium">
          We will process these details and create a risk profile for you,
          giving you the likelihood of you defaulting on your loan. To autofill,
          upload your credit report.
        </span>
      </div>

      <div className="flex flex-col mt-12">
        <label className="w-full cursor-grab relative bg-transparent border-2 border-white px-10 py-10 text-center flex justify-center rounded-lg">
          {loading ? (
            <CircularProgress color="primary" size="lg" />
          ) : (
            <div>
              <UploadIcon className="text-white me-4" />
              <span className="text-white">Select PDF</span>
              <input
                type="file"
                // onChange={(e) => {
                //   setFile(e.target.files[0]);
                //   console.log("File has been uploaded")

                //   setTimeout(function(){
                //     handleFile();
                //   }, 1000)
                // }}
                onChange={handleFile}
                placeholder="Upload File here"
                className="invisible absolute"
              />
            </div>
          )}
        </label>
        {/* <button
          type="button"
          className="w-fit mt-4 text-white border-2 border-white px-5 py-2 rounded-lg"
          onClick={handleFile}
        >
          Preload data
        </button> */}
      </div>

      <div className="mt-20 grid grid-cols-2 gap-x-32 gap-y-5">
        <div className="flex flex-col">
          <label htmlFor="age" className="text-white">
            Age:
          </label>
          <input
            type="number"
            name="age"
            value={formData.age}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.age && <span>{errors.age}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="income" className="text-white">
            Income:
          </label>
          <input
            type="number"
            name="income"
            value={formData.income}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.income && <span>{errors.income}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="loanAmount" className="text-white">
            Loan Amount:
          </label>
          <input
            type="number"
            name="loanAmount"
            value={formData.loanAmount}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.loanAmount && <span>{errors.loanAmount}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="creditScore" className="text-white">
            Credit Score:
          </label>
          <input
            type="number"
            name="creditScore"
            value={formData.creditScore}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.creditScore && <span>{errors.creditScore}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="monthsEmployed" className="text-white">
            Months Employed:
          </label>
          <input
            type="number"
            name="monthsEmployed"
            value={formData.monthsEmployed}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.monthsEmployed && <span>{errors.monthsEmployed}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="creditLines" className="text-white">
            Credit Lines:
          </label>
          <input
            type="number"
            name="creditLines"
            value={formData.creditLines}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.creditLines && <span>{errors.creditLines}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="interestRate" className="text-white">
            Interest Rate:
          </label>
          <input
            type="number"
            name="interestRate"
            value={formData.interestRate}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.interestRate && <span>{errors.interestRate}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="loanTerm" className="text-white">
            Loan Term:
          </label>
          <input
            type="number"
            name="loanTerm"
            value={formData.loanTerm}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.loanTerm && <span>{errors.loanTerm}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="debtToIncomeRatio" className="text-white">
            Debt To Income Ratio:
          </label>
          <input
            type="number"
            name="debtToIncomeRatio"
            value={formData.debtToIncomeRatio}
            onChange={handleInputChange}
            className="mt-2 rounded-xl w-full py-1 px-3"
          />
          {errors.debtToIncomeRatio && <span>{errors.debtToIncomeRatio}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="education" className="text-white mb-2">
            Level of Education:
          </label>
          <ReactSelect
            defaultValue={formData.education}
            onChange={(e) => {
              setFormData({
                ...formData,
                education: e.value,
              });
            }}
            options={educationOptions}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.education && <span>{errors.education}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="employmentType" className="text-white mb-2">
            Employment Type:
          </label>
          <ReactSelect
            defaultValue={formData.employmentType}
            onChange={(e) => {
              setFormData({
                ...formData,
                employmentType: e.value,
              });
            }}
            options={[
              { value: 1, label: "Full-time" },
              { value: 2, label: "Unemployed" },
              { value: 4, label: "Part-time" },
              { value: 3, label: "Self-employed" },
            ]}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.employmentType && <span>{errors.employmentType}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="maritalStatus" className="text-white mb-2">
            Marital Status:
          </label>
          <ReactSelect
            defaultValue={formData.maritalStatus}
            onChange={(e) => {
              setFormData({
                ...formData,
                maritalStatus: e.value,
              });
            }}
            options={[
              { value: 1, label: "Divorced" },
              { value: 2, label: "Married" },
              { value: 3, label: "Single" },
            ]}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.maritalStatus && <span>{errors.maritalStatus}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="mortgage" className="text-white mb-2">
            Mortgage:
          </label>
          <ReactSelect
            defaultValue={formData.mortgage}
            onChange={(e) => {
              setFormData({
                ...formData,
                mortgage: e.value,
              });
            }}
            options={booleanOptions}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.mortgage && <span>{errors.mortgage}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="dependents" className="text-white">
            Do you have dependents:
          </label>
          <ReactSelect
            defaultValue={formData.dependents}
            onChange={(e) => {
              setFormData({
                ...formData,
                dependents: e.value,
              });
            }}
            options={booleanOptions}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.dependents && <span>{errors.dependents}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="loanPurpose" className="text-white mb-2">
            Purpose of the Loan:
          </label>
          <ReactSelect
            defaultValue={formData.loanPurpose}
            onChange={(e) => {
              setFormData({
                ...formData,
                loanPurpose: e.value,
              });
            }}
            options={[
              { value: 2, label: "Auto" },
              { value: 5, label: "Education" },
              { value: 4, label: "Home" },
              { value: 3, label: "Business" },
              { value: 1, label: "Other" },
            ]}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.loanPurpose && <span>{errors.loanPurpose}</span>}
        </div>

        <div className="flex flex-col">
          <label htmlFor="coSigner" className="text-white mb-2">
            Do you have a Co-Signer:
          </label>
          <ReactSelect
            defaultValue={formData.coSigner}
            onChange={(e) => {
              setFormData({
                ...formData,
                coSigner: e.value,
              });
            }}
            options={booleanOptions}
            classNames={{
              option: (state) => "rounded-xl",
            }}
            theme={(theme) => ({
              ...theme,
              borderRadius: 12,
            })}
          />
          {errors.coSigner && <span>{errors.coSigner}</span>}
        </div>

        {/* Add similar input fields for other form inputs */}
      </div>
      <div className="flex flex-col items-center justify-center">
        <button
          type="submit"
          className="border-2 border-white w-1/2 mt-20 py-2 rounded-lg text-white"
        >
          View Score
        </button>
      </div>
    </form>
  );
};

export default LoanApplicationForm;
