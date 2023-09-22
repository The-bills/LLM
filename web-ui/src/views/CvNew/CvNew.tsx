import { useParams } from "react-router-dom"
import { Sidebar } from "../../components/Sidebar"
import { TextInput } from "../../components/Input"
import { useState } from "react"
import { useCvQuery } from "../../queries/useCvQuery"

const BE_URL = 'http://127.0.0.1:5000'

export const CvNew = () => {
    const { cvId } = useParams()
    const { data } = useCvQuery(cvId ?? '')
    const [name, setName] = useState('')
    const link = data?.filelink && `${BE_URL}/${data?.filelink}#toolbar=0&navpanes=0&scrollbar=0`

    return (
        <div className='flex items-stretch h-screen'>
            <Sidebar />
            <div className="flex-1 p-16">
                <h1 className='text-3xl font-bold'>Update CV</h1>
                <TextInput label="Name" value={data?.name ?? name} onChange={setName} className='mt-8' />
                <button className='mt-8 bg-slate-700 text-white px-4 py-2 rounded-md'>Save</button>
            </div>
            <div className="flex flex-1 p-16">
            <object className="flex-1 rounded-l shadow-slate-200 shadow-md" type="application/pdf" data={link} height="100%" />
            </div>
        </div>
    )
}