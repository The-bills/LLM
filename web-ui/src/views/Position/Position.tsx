import { useParams } from "react-router-dom"
import { PageWithNavbar } from "../../layouts/PageWIthNavbar"
import { usePositionQuery } from "../../queries/usePositionQuery"
import { usePositionScoreMutation } from "../../queries/usePositionScoreMutation"
import Skeleton from "react-loading-skeleton"
import 'react-loading-skeleton/dist/skeleton.css'
import { useState } from "react"

export const Position = () => {
    const { positionId } = useParams()
    const {data} = usePositionQuery(positionId ?? '')
    const mutation = usePositionScoreMutation(positionId ?? '')
    const [history, setHistory] = useState([] as any[])

    const handleClick = async () => {
        let res = await mutation.mutateAsync()
        if(!res) return
        setHistory(prev => [...prev, {
                id: Math.random(),
                inserted_at: (new Date()).toUTCString(),
                response: res.replaceAll('"', '')
            }])
    }

    console.log(history)
    
    return(
        <PageWithNavbar>
            <h1 className='text-3xl font-bold'>{data?.name}</h1>
            <div className=''>Position</div>
            <div className='mb-4 mt-4'>{data?.description}</div>
            <button onClick={handleClick} className='bg-slate-700 pt-2 pb-2 pl-3 pr-3 text-slate-100  font-semibold rounded'>Find canndidates</button>
            <div className='flex  flex-col items-stretch gap-4 pt-4'>
                {mutation.isLoading &&
                    <div className='border rounded-md p-5'>
                        <Skeleton count={3.2} className='self-stretch w-10' />
                    </div>}
                {history
                    .sort((a, b) => (new Date(b.inserted_at)).getTime() - (new Date(a.inserted_at)).getTime())
                    .map( his => 
                        <div key={his.response} className='border rounded-md p-5'>{his.response}</div>
                    )}
            </div>
        </PageWithNavbar>
    )
}