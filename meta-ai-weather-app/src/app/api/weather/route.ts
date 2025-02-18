import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const place = searchParams.get("place");

  if (!place) {
    return NextResponse.json({ error: "Missing place parameter" }, { status: 400 });
  }

  try {
    // Call your Python API
    const response = await fetch(`http://127.0.0.1:5000/weather?place=${encodeURIComponent(place)}`);
    const data = await response.json();

    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json({ error: "Failed to fetch weather" }, { status: 500 });
  }
}
