type Props = {
    name: string
}

export const ListRow = (p: Props) => {
    return (
        <div className='grid rows-2 border-b-2 pb-5 mt-5'>
            <div className='text-base font-semibold pb-1'>{p.name}</div>
            <div className='text-sm text-slate-700'>Sep 11, 2023</div>
        </div>
    )
}