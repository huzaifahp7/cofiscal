"use client";
import { useEffect, useState } from "react";
import { Skeleton } from "@nextui-org/react";

const Analysis = ({ result }) => {
  return (
    <div className="w-full rounded-lg">
      <span className="text-white tracking-widest text-lg">
        {result.predict[0]}
      </span>

      <ul>
        {result.predict.slice(1, 4).map((item) => {
          return (
            <li key={item} className="mt-4">
              <span className="text-white tracking-widest text-lg">{item.replaceAll('*', '')}</span>
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Analysis;
