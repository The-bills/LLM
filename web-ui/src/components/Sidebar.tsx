import { Link } from "react-router-dom"
import { DocumentIcon, HomeIcon, JobIcon } from "../assets/icons"

export const Sidebar = () => {
    return (
        <div className='h-screen w-72  border-r-2 bg-slate-900 pt-12'>
            <div className='flex flex-col p-10 gap-5 text-slate-400 font-semibold'>
                <div className='flex flex-row'>
                    <HomeIcon />
                    <Link className='ml-2' to='/'>Home</Link>
                </div>
                <div className='flex flex-row '>
                    <DocumentIcon />
                    <Link className='ml-2' to='/cv'>CVs</Link>
                </div>
                <div className='flex flex-row'>
                    <JobIcon />
                    <Link className='ml-2' to='/positions'>Positions</Link>
                </div>
            </div>
        </div>
    )
}