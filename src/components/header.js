import Image from "next/image";

const Header = () => {
  return (
    <div className="absolute flex flex-row-reverse items-center gap-x-6 top-0 right-0 w-1/2 h-20 mt-4 me-10 ">
      <Image
        src={"/images/profile.jpg"}
        alt="profile image"
        height={80}
        width={80}
        className="rounded-full aspect-square"
      ></Image>

      <div className="w-1 h-20 bg-white rounded-3xl me-6"></div>

      <span className="text-2xl text-white font-normal me-10">About Us</span>
      <span className="text-2xl text-white font-normal me-10">History</span>
    </div>
  );
};

export default Header;
