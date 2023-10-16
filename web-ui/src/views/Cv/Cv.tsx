import { useNavigate, useParams } from "react-router-dom"
import { Sidebar } from "../../components/Sidebar"
import { TextInput } from "../../components/Input"
import { useState } from "react"
import { useCvQuery } from "../../queries/useCvQuery"
import { useDeleteCvQuery } from "../../queries/useDeleteCvQuery"

const BE_URL = 'http://127.0.0.1:5000'

export const Cv= () => {
    const { cvId } = useParams()
    const { data } = useCvQuery(cvId ?? '')
    const { mutateAsync: deleteCv } = useDeleteCvQuery()
    const link = data?.filelink && `${BE_URL}/${data?.filelink}#toolbar=0&navpanes=0&scrollbar=0`
    const navigate = useNavigate()

    const handleDelete = async () => {
        const areYouSure = window.confirm('Are you sure you want to delete this CV?')
        if(!areYouSure) return
        await deleteCv(cvId ?? '')
        navigate('/cv/')
    }

    const openFile = () =>{
        if(!link) return
        window.open(link, '_blank')
    }

    return (
        <div className='flex items-stretch h-screen'>
            <Sidebar />
            <div className="flex-1 p-16">
                <h1 className='text-3xl font-bold'>CV Details</h1>
                <TextInput disabled label="Name" value={data?.name} className='mt-8' />
                <TextInput disabled label="Education" value={data?.metadata.education} className='mt-8' />

                <button className='mt-8 bg-slate-700 text-white px-4 py-2 rounded-md' onClick={openFile}>View File</button>
                <button disabled className='mt-8 bg-slate-700 text-white px-4 py-2 rounded-md ml-2'>Edit</button>
                <button className='mt-8 bg-slate-700 text-white px-4 py-2 rounded-md ml-2' onClick={handleDelete}>Delete</button>
            </div>
            <div className="flex flex-1 p-16">
                <object className="flex-1 rounded-l shadow-slate-200 shadow-md" type="application/pdf" data={link} height="100%" />
            </div>
        </div>
    )
}