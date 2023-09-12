import { Sidebar } from "../components/Sidebar"

export const PageWithNavbar = (p: { children: React.ReactNode }) => (
    <div className="flex flex-row">
        <Sidebar />
        <div className='flex-1 p-16'>{p.children}</div>
    </div>
)
